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
config.read("backend/config.ini")
response = json.loads(requests.get(config.get("DEFAULT", "API_URL")).text)

if os.path.isfile('backend/trained_model'):
    with open('backend/trained_model', 'rb') as file:
        model = pickle.load(file)

else:
    database = pandas.read_csv(config.get(
        "DEFAULT", "API_DATABASE_1H"), header=1)

    X = database.loc[:, ['Open', 'High', 'Low']]
    Y = database.loc[:, ['Close']]

    model = linear_model.LinearRegression().fit(X, Y)

    with open('backend/trained_model', 'wb') as file:
        pickle.dump(model, file)

    validation_base = database.sample(frac=.2).loc[:, ['Open', 'High', 'Low']]

    database.to_csv('backend/gemini_database_1hr.csv', index=False)
    validation_base.to_csv(
        'backend/gemini_database_1hr_testing.csv', index=False)

X = pandas.read_csv('backend/gemini_database_1hr_testing.csv').values.tolist()

Y_new = model.predict(X)

for i in range(len(X)):
    print(f"Linha {i} - {X[i]} Previsão do Close = {Y_new[i]}")
