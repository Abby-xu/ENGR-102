# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 9b
# Date:		    30/10/2019
from matplotlib import pyplot as plt
import csv
import numpy as np
#####import data#####
with open('Lab10/Lab10b/WeatherDataMac.csv', 'r') as weather_data:
    date = []
    temp_avg = []
    pressure_avg = []
    avgtemp = []
    avgpressure = []
    eachlines = csv.reader(weather_data) 
    for row in eachlines:
        date.append(row[0])
        temp_avg.append(row[2])
        pressure_avg.append(row[11])
    date.pop(0)
    temp_avg.pop(0)
    pressure_avg.pop(0)
    for value in temp_avg:
        avgtemp.append(float(value))
    for value1 in pressure_avg:
        avgpressure.append(float(value1))
#####draw the graph#####
fig = plt.figure(figsize = (25,10))
ax = fig.add_subplot()
ax2 = ax.twinx()
ax.set_title('average temp and pressure in 2016')
a = ax.plot(avgtemp, '-', label = 'pressure_avg')
b = ax2.plot(avgpressure, '-', label = 'temperature_avg',color="red")
ax.grid()
ax.set_xlabel("Days")
ax.set_ylabel(r"Pressure")
ax2.set_ylabel(r"Temperature")
lns = a + b
labs = [l.get_label() for l in lns]
ax2.legend(lns, labs, loc=0)
plt.show('avg_temp&pressure_2016.png')