# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 10b
# Date:		    30/10/2019
from matplotlib import pyplot as plt
import csv
import numpy as np
date = []
temp_high = []
temp_avg = []
temp_low = []
weather_data = open('/Users/abby/Desktop/ENGR102_554/Lab10/Lab10b/WeatherDataMac.csv', 'r')
#####import data for x, y1 and y2#####
eachlines = csv.reader(weather_data) 
for row in eachlines:
    date.append(row[0])
    temp_high.append(row[1])
    temp_avg.append(row[2])
    temp_low.append(row[3])
date.pop(0)
temp_avg.pop(0)
temp_high.pop(0)
temp_low.pop(0)
weather_data.close()
#print(len(date))

data = [[],[],[],[]]
for a in range(2015,2018):
    for i in range(1,13):
        determine_avg = []
        determine_high = []
        determine_low = []
        for k in range(len(date)):
            if int(date[k][-4:]) == a:
                #print(date[k][-1])
                if date[k][1] != '/' and (int(date[k][0] + date[k][1])) == i:
                    determine_avg.append(int(temp_avg[k]))
                    determine_high.append(int(temp_high[k]))
                    determine_low.append(int(temp_low[k]))
                elif int(date[k][0]) == i:
                    #print(k)
                    determine_avg.append(int(temp_avg[k]))
                    determine_high.append(int(temp_high[k]))
                    determine_low.append(int(temp_low[k]))

        data[0].append([a,i])
        data[1].append(sum(determine_avg)/len(determine_avg))
        data[2].append(max(determine_high))
        data[3].append(min(determine_low))
        determine_avg.clear()
        determine_high.clear()
        determine_low.clear()
print(data[2])
print(data[3])
'''
fig, ax = plt.subplots()
index = np.arange(len(data[0]))
bar_width = 0.35
opacity = 0.8

error_attri = dict(elinewidth = 2, ecolor="y", capsize = 3)
plt.bar(index, data[1], bar_width, alpha = opacity, color = 'c', label = 'everangetemp', yerr = np.array(data[3]),error_kw=error_attri)
#plt.errorbar(data[0],data[1],yerr = data[2] - data[3],fmt='o',ecolor='r',color='b',elinewidth=2,capsize=4)
#plt.errorbar(data[0], data[1], yerr = np.array(data[3]),color = 'k')
#rects2 = plt.bar(index + bar_width, data[2], bar_width, alpha=opacity, color='m', label='highesttemp')
#rects3 = plt.bar(index + bar_width + bar_width, data[3], bar_width, alpha=opacity, color='r', label='lowesttemp')
#rects3 = plt.bar(index + bar_width + bar_width + bar_width, data[4], bar_width, alpha=opacity, color='c', label='error bar')

plt.xlabel('month')
plt.ylabel('temperature')
plt.title('the temperature in 2015-2017')
#index + bar_width, tuple(data[0]),rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
'''