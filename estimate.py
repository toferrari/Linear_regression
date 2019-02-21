#!/usr/bin/env python3

import csv
import matplotlib as plt

km = 0
while km <= 0:
	try:
		km = int(input("Enter your Km ?\n"))
		if km <= 0:
			print("Please use positive number")
	except:
		print("Please use a number")
		continue
theta = list()
try:
	data = csv.reader(open("theta.csv", "r"))
	for row in data:
		try:
			theta.append(float(row[0]))
			theta.append(float(row[1]))
		except:
			print ("Error")
except:
	theta = [0,0]

print ("The estimation for", km, "km, is", int(float(km) * theta[1] + theta[0]), "$.")
