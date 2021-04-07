import pandas 
from sklearn import linear_model
import sqlalchemy
import requests
import json
import pickle
import os.path
import csv
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
#response = json.loads(requests.get(config.get("DEFAULT", "API_URL")).text)
response = json.loads(requests.get("https://api.gemini.com/v2/ticker/btcusd").text)

if os.path.isfile('backend/trained_model'):
    with open('backend/trained_model', 'rb') as file:
        model = pickle.load(file)

else:
    # df = pandas.read_csv("BASE_URL")
    database = pandas.read_csv("https://www.cryptodatadownload.com/cdd/gemini_BTCUSD_1hr.csv", header=1)
    database['Date'] = pandas.to_datetime(database['Date'])
    database = database.sort_values(by='Date')
    colunas_x = ['Open','High','Low']
    X = database.loc[:, colunas_x]
    Y = database.loc[:, ['Close']]
    model = linear_model.LinearRegression()
    model.fit(X, Y)
    with open('backend/trained_model', 'wb') as file:
        pickle.dump(model, file)
    #salvando o banco
    database.to_csv('backend/database_1hr.csv')

# X = list(csv.reader(open('D:\Downloads\gemini_BTCUSD_1hr_editado.csv')))
#Puxando da api e prevendo com o modelo gerado
response = requests.get("https://api.gemini.com/v2/candles/btcusd/1hr")
btc_new_data = json.loads(response.text)
btc_new_data.reverse()
iterator = iter(btc_new_data)
for i in iterator:
        try:
            #print(next(iterator))
            i = next(iterator)
            oopen = i[1]
            high = i[2]
            low = i[3]
            close = i[4]
            close_prediction = model.predict([[oopen, high, low]])
            print("open:", oopen, "high:", high, "low:", low, "close:", close, "Previsão:", close_prediction,
            "Diferença:", close - close_prediction)
        except:
            print('O último fechamento do Bitcoin: ', close_prediction)

# Y_new = model.predict(X)

# for i in range(len(X)):
#     print(f"Linha {i} - {X[i]} Previsão do Close = {Y_new[i]}")