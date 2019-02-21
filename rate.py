#!/usr/bin/env python3

import csv
import sys
import numpy
import matplotlib.pyplot as plt

def check_list(km, price, m):
	for i in range(m):
		if type(km[i]) != float or type(price[i]) != float:
			return False
	return True

def first_theta0(km, price, m):
	tmp = price[0]
	tmp_km = km[0]
	for i in range(m):
		if (tmp_km > km[i] and tmp < price[i]):
			tmp = price[i]
	return (tmp)

def new_grad(hold, m):
	tmp = 0.0
	km = list()
	for i in range(m):
		if hold[i] > tmp:
			tmp = hold[i]
	for j in range(m):
		km.append(hold[j] / tmp)
	return km, tmp

def estimate(theta0, theta1, X):
	return (theta0 + (theta1 * X))

def derivate(m, km, price, theta0, theta1):
	ret = 0.0
	tmp = 0.0
	for i in range(m):
		tmp = (estimate(theta0, theta1, km[i]) - price[i])
		ret += tmp * tmp
	ret /= (2 * float(m))
	return ret

def fct_thetha0(m ,km, price, theta0, theta1):
	ret = 0.0
	for i in range(m):
		ret += (estimate(theta0, theta1, km[i]) - price[i])
	return ret

def fct_thetha1(m ,km, price, theta0, theta1):
	ret = 0.0
	for i in range(m):
		ret += ((estimate(theta0, theta1, km[i]) - price[i]) * km[i])
	return ret

def learnningRate(m):
	return (0.1)

def file_thetha(theta0, theta1):
	fthetha = open("theta.csv", "w")
	fthetha.write(str(theta0) + "," + str(theta1))
	fthetha.close()

def graph(km, price, theta0, theta1):
	plt.plot([km],[price], 'ro', markersize=4)
	plt.plot([estimate(theta0, theta1, x) for x in range(250000)], \
	 												"b", linewidth=3)
	plt.xlabel('Mileage')
	plt.ylabel('Price')
	plt.show()

def cost(m ,km, price, theta0, theta1):
	ret = 0.0
	for i in range(m):
		ret += (estimate(theta0, theta1, km[i]) - price[i])**2
	ret = ret/(2*m)
	return ret

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#				Programme
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

data = csv.reader(open("data.csv", "r"))
km, price = list(), list()
for row in data:
	try:
		km.append(float(row[0]))
		price.append(float(row[1]))
	except:
		km.append(row[0])
		price.append(row[1])
del km[0], price[0]
m = len(km)
fl_m = float(m)
if check_list(km, price, m) == False:
	print ("error")
	sys.exit(-1)
theta0, theta1, i = 0.0, 0.0, 0
nomre_km, max_km = new_grad(km, m)
norme_price, max_price = new_grad(price, m)
while (cost(m, nomre_km, norme_price, theta0, theta1)> 0.0032475):
	tmp_theta0 = learnningRate(fl_m) * (1 / fl_m) * \
				(fct_thetha0(m, nomre_km, norme_price, theta0, theta1))
	tmp_theta1 = learnningRate(fl_m) * (1 / fl_m) * \
				(fct_thetha1(m, nomre_km, norme_price, theta0, theta1))
	theta0 = theta0 - tmp_theta0
	theta1 = theta1 - tmp_theta1
file_thetha(theta0 * max_price , theta1 * max_price / max_km)
graph(km, price, theta0 * max_price, theta1 * max_price / max_km)
