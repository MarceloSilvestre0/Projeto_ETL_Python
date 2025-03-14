 
<p align="center">
  <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeW9pZ3E5bTNxend1ZmV1MWV2aTFxM3Y4d2RzempmcGZmc3FsbHYyNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fhAwk4DnqNgw8/giphy.gif" alt="Imagem"></a>
</p>

# 💰 **Data Pipeline: Extração de Dados Bitcoin com ETL em Python**  

## **Introdução**  

Este projeto faz parte da minha rotina de estudos. A intesão desse respositório é demonstrar uma parcela do que estou aprendendo e, mais importante de tudo, buscar opiniões, criticas e sugestões de melhorias nos meus códigos, estruturas e métodos de desenvolvimento. 

Motivação:  
1. Aprimoramento de habilidades como: estrutura de dados, algoritmos e versionamento de código.  
2. Conhecer novas tecnologias, frameworks, classes, métodos e boas práticas em projetos de dados.
3. Construir e aprimorar um pensamento analitico e tecnico que proporcione insights e soluções simples e funcionais.

## **Overview do Projeto**  

### **Objetivo Principal**  
Desenvolver um pipeline ETL automatizado para consumir dados da **API da Coinbase** e armazenar informações sobre o preço da Bitcoin ao longo do tempo.  

### **Etapas do Projeto**  

1. **Extração (E)**:  
   - Utilizar a **API da Coinbase** para obter o preço atual da Bitcoin.  
   - Trabalhar com os endpoints públicos da API (sem necessidade de autenticação).  

2. **Transformação (T)**:  
   - Selecionar apenas as informações relevantes: preço da Bitcoin, horário da consulta e moeda de referência (USD).  
  
3. **Carga (L)**:  
   - Armazenar os dados coletados em um banco de dados SQL.  

4. **Automatização**:  
   - Agendar o programa para executar periodicamente (por exemplo, a cada hora ou diariamente), garantindo a coleta contínua dos dados.  

---

## **Tecnologias Utilizadas**  
- **Python 3.12**  
- **Bibliotecas**:  
   - `requests`: Para consumir APIs.  
   - `pandas`: Para manipulação e organização de dados.  
   - `sqlite3`: Para armazenamento em banco de dados (opcional).  
   - `tinydb`: Para armazenamento em banco de dados NoSQL.
   - `sqlalchemy`: SQLAlchemy é uma biblioteca de mapeamento objeto-relacional para Python.
   - `psycopg2-binary`: Psycopg é uma biblioteca de acesso a dados PostgreSQL para Python.
   - `streamlit`: Para criar dashboards interativos.
   - `time`: Para medir o tempo de execução do programa.
   - `datetime`: Para manipulação de datas e horas.
- **Coinbase API**: Para obter o preço da Bitcoin em tempo real.  

---

## **Exemplo de Dados Coletados**  
| Data/Hora           | Preço (USD) | Moeda   |  
|----------------------|------------|---------|  
| 2024-01-01 12:00:00 | 42,000.50  | Bitcoin |  
| 2024-01-01 13:00:00 | 42,150.75  | Bitcoin |  

---

## **Resultados Esperados**  
Ao final deste projeto, é esperado que a solução:  
1. Extraia os dados via API da Coinbase  
2. Transformae e organize os dados em formato estruturado.
3. Armazene os dados coletados em um banco de dados personalizado.  
4. Realize o processo de ETL através do pipeline automatizado.  

## **Próximos Passos**    
1. **Transformação Avançada**: Limpeza e enriquecimento dos dados.  
2. **Armazenamento Persistente**: Ingestão em bancos de dados em nuvem.  
3. **Visualização de Dados**: Construção de dashboards interativos.
4. **Machine Learning**: Implementação de modelos de ML como: Regressão Linear, Árvores de Decisão, Random Forest ou XGBoost  
