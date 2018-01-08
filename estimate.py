#!/usr/bin/python3.4

import csv
import matplotlib.pyplot as plt

# file = open("data.csv", "rb")
km = 0
while km <= 0:
	try:
		km = int(input("Quel est votre nombre de km ?\n"))
		if km <= 0:
			print("Please choose a positive number")
	except:
		print("Please use a number")
		continue
