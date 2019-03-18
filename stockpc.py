import csv
import numpy as ny
from sklearn import linear_model

dates = []
prices = []


def get_data():
	stockpr = open('stock4.txt', "r")
	csvFileReader = csv.reader(stockpr)
	day=0
	for row in csvFileReader:
		dates.append(int(row[0]))
		prices.append(float(row[1]))
	
	return dates[-1]

def predict_price(dates,prices,x):
	linear_mod = linear_model.LinearRegression() #defining the linear regression model
	dates = ny.reshape(dates,(len(dates),1)) # converting to matrix of n X 1
	prices = ny.reshape(prices,(len(prices),1))
	linear_mod.fit(dates,prices) #fitting the data points in the model
	predicted_price =linear_mod.predict(x)
	return predicted_price[0][0]


def Articlesc():
        articlesc=[]
        day=get_data() # calling get_data method by passing the csv file to it
        for i in range(7):
                predicted_price = predict_price(dates,prices,day+i)
                articlesc.append(str(predicted_price))
        return articlesc

Articlesc()

