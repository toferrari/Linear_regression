#!/usr/bin/python3.4

import csv

data = csv.reader(open("data.csv", "r"))
for row in data:
	print(row)
