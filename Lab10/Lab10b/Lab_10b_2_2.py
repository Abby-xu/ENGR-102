# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 9b
# Date:		    29/10/2019
from matplotlib import pyplot as plt
import csv
import numpy as np
date = []
precipitation = []
pre = []
weather_data = open('/Users/abby/Desktop/ENGR102_554/Lab10/Lab10b/WeatherDataMac.csv', 'r')
#####import data for x, y#####
eachlines = csv.reader(weather_data) 
for row in eachlines:
    precipitation.append(row[13])
precipitation.pop(0)
for value in precipitation:
    pre.append(float(value))

weather_data.close()
'''
#####sort data for days and precipitation#####
a = {}
for i in precipitation:
    if precipitation.count(i)>1:
        a[i] = precipitation.count(i)
a = sorted(a.items(), key=lambda item:item[0])
#print (a)
x = []
y = []
i = 0
while i != len(a):
    data = a[i]
    x.append(float(data[0]))
    y.append(data[1])
    i += 1
print(x)
print(y)
'''
n, bins, patches = plt.hist(pre, 'auto', facecolor = 'blue', alpha = 0.5)
plt.xlim((-0.01, 0.6))
plt.ylim((0, 30))
plt.show()
