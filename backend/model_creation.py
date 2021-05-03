import pandas
from sklearn import linear_model
import json
import numpy
import requests
import configparser

config = configparser.ConfigParser()
config.read("backend/config.ini")

database = pandas.read_csv(config.get(
    "DEFAULT", "API_DATABASE_1H"), header=1)

X = database.loc[:, ['Open', 'High', 'Low']]
Y = database.loc[:, ['Close']]

model = linear_model.LinearRegression().fit(X, Y)

api_response = json.loads(requests.get(
    config.get("DEFAULT", "API_URL")).text)

close_predict = model.predict(
    [[api_response['open']] + [api_response['high']] + [api_response['low']]])


def prediction():

    return(close_predict[0], api_response['open'])
