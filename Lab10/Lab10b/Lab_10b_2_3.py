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
date = []
temp_avg = []
dew_avg = []
changetemp = []
changedew = []
weather_data = open('/Users/abby/Desktop/ENGR102_554/Lab10/Lab10b/WeatherDataMac.csv', 'r')
#####import data for x, y1 and y2#####
eachlines = csv.reader(weather_data) 
for row in eachlines:
    date.append(row[0])
    temp_avg.append((row[2]))
    dew_avg.append((row[5]))
date.pop(0)
temp_avg.pop(0)
dew_avg.pop(0)
for value in temp_avg:
    changetemp.append(float(value))
for value1 in dew_avg:
    changedew.append(float(value1))
weather_data.close()

fig=plt.figure(figsize=(6,6))
plt.scatter(changetemp,changedew)
plt.grid(True)#show the grid
plt.axis("equal")#make the length of x as same as y
plt.title("relationship between temp and dew") 
plt.xlabel("x")
plt.ylabel("y")
plt.show(fig)