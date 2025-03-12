import time
import requests
from tinydb import TinyDB
from datetime import datetime as dt

def data_bitcoin():
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    data = response.json()
    return data

def bitcoin_data_transform(data):
    value = data["data"]["amount"]
    cripto = data["data"]["currency"]
    coin = data["data"]["base"]
    timestamp=dt.now().timestamp()
     
    transformed_data = {
        "value":value,
        "cripto":cripto,
        "coin":coin,
        "timestamp":timestamp
     }
    return transformed_data

def tinydb_data_save(data, db_name="bitcoin.json"):
    db=TinyDB(db_name)
    db.insert(data) 
    print("Dados salvos com sucesso")

if __name__=="__main__":
    #Extração dos dados
    while True:
        data_json = data_bitcoin()
        data_transformed = bitcoin_data_transform(data_json)
        tinydb_data_save(data_transformed)
        time.sleep(15)
        