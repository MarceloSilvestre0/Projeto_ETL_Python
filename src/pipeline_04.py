import time
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from dotenv import load_dotenv
import os

from database import Base, BitcoinPreco

# Carrega as variáveis de ambiente do arquivo .env (sem SSL)
load_dotenv()

# Lê as variáveis de ambiente do arquivo .env
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Monta a URL de conexão com o banco de dados PostgreSQL
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# Cria o engine de conexão com o banco e a sessão para manipular os dados
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_table():
    """Cria a tabela no banco de dados, se ela não existir."""
    Base.metadata.create_all(engine)
    print("Tabela criada com sucesso")


def data_bitcoin():
    """Faz uma requisição à API do Coinbase para obter o preço do Bitcoin."""
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    data = response.json()
    return data


def bitcoin_data_transform(data):
    """Transforma os dados extraídos para o formato desejado."""
    value = data["data"]["amount"]  # Preço atual do Bitcoin
    cripto = data["data"]["currency"]  # Moeda (USD, EUR, etc.)
    coin = data["data"]["base"]  # Criptomoeda (BTC)
    timestamp = datetime.now()  # Marca o horário da extração
    
    # Retorna os dados transformados em formato de dicionário
    transformed_data = {
        "value": value,
        "cripto": cripto,
        "coin": coin,
        "timestamp": timestamp
    }
    return transformed_data


def data_save_postegres(data):
    """Salva os dados transformados no banco de dados PostgreSQL."""
    session = Session()
    new_reg = BitcoinPreco(**data)  # Cria um novo registro com os dados
    session.add(new_reg)  # Adiciona à sessão
    session.commit()  # Salva no banco
    session.close()  # Fecha a sessão
    print(f"[{data['timestamp']}] Dados salvos no PostgreSQL")


if __name__ == "__main__":
    # Cria a tabela no banco se não existir
    create_table()
    print("Iniciando ETL com atualização a cada 15 segundos... Use CTRL+C para interromper")
    
    # Loop principal do ETL
    while True:
        try:
            # Extração dos dados da API
            data_json = data_bitcoin()
            if data_json:
                # Transformação dos dados extraídos
                processed_data = bitcoin_data_transform(data_json)
                print("Dados tratados", processed_data)
                
                # Carregamento dos dados transformados no banco
                data_save_postegres(processed_data)

            # Espera 15 segundos antes da próxima execução
            time.sleep(15)

        # Captura a interrupção manual (CTRL+C) para encerrar o loop
        except KeyboardInterrupt:
            print("\nProcesso interrompido pelo usuário. Finalizando...")
            break
        
        # Captura outros erros para não parar a execução
        except Exception as e:
            print(f"Erro durante a execução: {e}")
            time.sleep(20)  # Espera mais tempo para evitar chamadas contínuas em caso de erro
