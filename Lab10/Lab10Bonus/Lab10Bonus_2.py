# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 9bonus
# Date:		    30/10/2019
from matplotlib import pyplot as plt
import numpy as np
import math
#####     1     #####
maxtemp = []
mintemp = []
avgtemp = []
avghumi = []
precipitation = []
with open('Lab10/Lab10Bonus/WeatherDataMac.csv') as csv:
    for line in csv.readlines():
        array = line.split(',')
        maxtemp.append(array[1])
        avgtemp.append(array[2])
        mintemp.append(array[3])
        avghumi.append(array[8])
        precipitation.append(array[13])
maxtemp.pop(0)
avgtemp.pop(0)
mintemp.pop(0)
avghumi.pop(0)
precipitation.pop(0)
print('the maximum and minimum temperature seen over the 3 year period are:',max(maxtemp),'and',min(mintemp))

#####     2     #####
pre = []
for value in precipitation:
    pre.append(float(value))
print('the average daily precipitation is:','%.2f'%(sum(pre)/len(pre)))
print('----------')

#####     3_1     #####
#ques:what is the relationship between temp and humidity?
temp_avg = []
humi_avg = []
for value in avgtemp:
    temp_avg.append(float(value))
for value in avghumi:
    humi_avg.append(float(value))

#draw the graph
fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.set_title('the relationship between temp and humidity')
index = np.arange(len(humi_avg))
bar_width=0.3
a = ax.bar(index,humi_avg,bar_width, label = 'humidity_avg', color='b')
b = ax2.plot(temp_avg, '-', label = 'pressure_avg',color="red")
ax.grid()
ax.set_xlabel("Days")
ax.set_ylabel(r"humidity(%)")
ax.legend()
ax2.set_ylabel(r"Temperature")
ax2.legend()
plt.show()

#####    3_2     #####
#Calculate the percentage of days when the humidity was above 90%
above = []
for i in range(len(humi_avg)):
    if humi_avg[i] >= 90:
        above.append(humi_avg[i])
print('the percentage of days when the humidity was above 90%:', '%.2f'%(len(above)/len(humi_avg)*100),'%')
print('----------')

#####     3_3     #####
#Calculate the mean and standard deviation of precipitation levels
print('the mean of daily precipitation is:','%.2f'%(sum(pre)/len(pre)))
a = []
for i in range(len(pre)):
    a.append((pre[i] - sum(pre)/len(pre))**2)
print('the satndard deviation is:','%.2f'%(math.sqrt(sum(a)/len(a))))