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
config.read("backend\config.ini")

response = json.loads(requests.get(config.get("DEFAULT", "API_URL")).text)

if os.path.isfile('trained_model'):
    with open('trained_model', 'rb') as file:
        model = pickle.load(file)

else:
    engine = sqlalchemy.create_engine(config.get("DEFAULT", "MYSQL_URI"))

    X = pandas.read_sql_table('bitcoin_history_hourly', engine,
                              columns=["open", "high", 'low'])
    Y = pandas.read_sql_table('bitcoin_history_hourly', engine,
                              columns=["close"])

    model = linear_model.LinearRegression()
    model.fit(X, Y)

    close_prediction = model.predict(
        [[response['open'], response['high'], response['low']]])
    
    with open('trained_model', 'wb') as file:
        pickle.dump(model, file)

X = list(csv.reader(open('D:\Downloads\gemini_BTCUSD_1hr_editado.csv')))
Y_new = model.predict(X)

for i in range(len(X)):
    print(f"Linha {i} - {X[i]} Previsão do Close = {Y_new[i]}")