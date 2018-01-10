#!/usr/bin/python3.4

import csv
import matplotlib.pyplot as plt

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
	return km

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
	return (0.01)

def graph(km, price, theta0, theta1):
	plt.plot([km],[price], 'ro', markersize=4)
	plt.plot([estimate(theta0, theta1, x) for x in range(2)], "b", linewidth=3)
	plt.xlabel('Mileage')
	plt.ylabel('Price')
	plt.show()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#ne pas oubleir de bien gerer le parsing
#regarder le generateur boucle for
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

data = csv.reader(open("data.csv", "r"))
hold_km = list()
hold_price = list()
for row in data:
	try:
		hold_km.append(float(row[0]))
		hold_price.append(float(row[1]))
	except:
		hold_km.append(row[0])
		hold_price.append(row[1])
del hold_km[0]
del hold_price[0]
m = len(hold_km)
fl_m = float(m)
theta0 = 0.0
theta1 = 0.0
i = 0
km = new_grad(hold_km, m)
price = new_grad(hold_price, m)
while i < 10000:
	tmp_theta0 = learnningRate(fl_m) * (1 / fl_m) * (fct_thetha0(m, km, price, theta0, theta1))
	tmp_theta1 = learnningRate(fl_m) * (1 / fl_m) * (fct_thetha1(m, km, price, theta0, theta1))
	theta0 = theta0 - tmp_theta0
	theta1 = theta1 - tmp_theta1
	# print("theta0 = {}, theta1 = {}".format(theta0, theta1))
	i += 1
print("theta0 = {}, theta1 = {}".format(theta0, theta1))
theta1 *= 8290.0 / 240000.0
theta0 *= 8290
i = estimate(theta0 , theta1 , float(42000))
print i
print theta1
# graph(km, price, theta0, theta1)
