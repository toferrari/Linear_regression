#!/usr/bin/python3.4

import csv
import matplotlib.pyplot as plt

km = 0
while km <= 0:
	try:
		km = int(input("Quel est votre nombre de km ?\n"))
		if km <= 0:
			print("Merci de saisir un chiffre posotif")
	except:
		print("Merci de mettre un nombre")
		continue
theta = list()
try:
	data = csv.reader(open("theta.csv", "r"))
	for row in data:
		try:
			theta.append(float(row[0]))
			theta.append(float(row[1]))
		except:
			print "erreur"
except:
	theta = [0,0]
print int(float(km) * theta[1] + theta[0])
