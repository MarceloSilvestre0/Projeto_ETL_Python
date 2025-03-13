import time
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from dotenv import load_dotenv
import os

from database import Base, BitcoinPreco

#Carrega as variaveis separadas do arquivo .env (sem SSL)
load_dotenv()

#Lê as variaveis separadas do arquivo .env (sem SSL)
POSTGRES_USER=os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST=os.getenv("POSTGRES_HOST")
POSTGRES_PORT=os.getenv("POSTGRES_PORT")
POSTGRES_DB=os.getenv("POSTGRES_DB")

#Concatena as informações do meu banco de dados criando a URL dele
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

#Cria o engine e a sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_table():
    """Cria a tebela no banco de dados, se não existir"""
    Base.metadata.create_all(engine)
    print("Tabela criada com sucesso")

def data_bitcoin():
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    data = response.json()
    return data

def bitcoin_data_transform(data):
    value = data["data"]["amount"]
    cripto = data["data"]["currency"]
    coin = data["data"]["base"]
    timestamp=datetime.now()
     
    transformed_data = {
        "value":value,
        "cripto":cripto,
        "coin":coin,
        "timestamp":timestamp
     }
    return transformed_data

def data_save_postegres(data):
    """Salva os dados no banco de PostgreSQL"""
    session = Session()
    new_reg = BitcoinPreco(**data)
    session.add(new_reg)
    session.commit()
    session.close()
    print(f"[{data['timestamp']}] Dados salvos no PostegreSQL")

if __name__=="__main__":
    create_table()
    print("Iniciando ETL com atualização a cada 15 segundos... Use CTRL+C para interromper")
    #Extração dos dados
    while True:
        try:
            data_json = data_bitcoin()
            if data_json:
                processed_data = bitcoin_data_transform(data_json)
                print("Dados tratados",processed_data)
                data_save_postegres(processed_data)
            time.sleep(15)
        except KeyboardInterrupt:
            print("\nProcesso interrompido pelo usuário. Finalizando...")
            break
        except Exception as e:
            print(f"Erro durante a execução: {e}")
            time.sleep(20)
        