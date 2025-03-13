from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, String, Integer, DateTime
from datetime import datetime

#Instância a classe Base do SQLAlchemy (na versão 2.x)
Base = declarative_base()

class BitcoinPreco(Base):
    """Define a tabela no banco de dados"""
    __tablename__ = "bitcoin_precos"

    id=Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=True)
    cripto = Column(String(50), nullable=True) #Restringe a quantidade de caracteres nas células da coluna para 50
    coin = Column(String(4), nullable=True)
    timestamp = Column(DateTime, default=datetime.now)