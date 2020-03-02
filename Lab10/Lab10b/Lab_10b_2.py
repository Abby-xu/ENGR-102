# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 9b
# Date:		    30/10/2019
import csv
import numpy as np
from matplotlib import pyplot as plt
#####import data#####
with open('Lab10/Lab10b/WeatherDataMac.csv', 'r') as weather_data:
#####graph 1 lists#####
    date = []
    temp_avg = []
    pressure_avg = []
    avgtemp = []
    avgpressure = []
#####graph 2 lists#####
    precipitation = []
    pre = []
#####graph 3 lists#####
    dew_avg = []
    avgdew = []
#####graph 4 lists#####
    temp_high = []
    temp_low = []
#####import form csv file#####
    eachlines = csv.reader(weather_data) 
    for row in eachlines:
        date.append(row[0])
        temp_high.append(row[1])
        temp_avg.append(row[2])
        temp_low.append(row[3])
        dew_avg.append(row[5])
        pressure_avg.append(row[11])
        precipitation.append(row[13])

date.pop(0)
temp_high.pop(0)
temp_avg.pop(0)
temp_low.pop(0)
dew_avg.pop(0)
pressure_avg.pop(0)
precipitation.pop(0)

for value in temp_avg:
    avgtemp.append(float(value))
for value in dew_avg:
    avgdew.append(float(value))
for value in pressure_avg:
    avgpressure.append(float(value))
for value in precipitation:
    pre.append(float(value))

#####graph 1#####
fig = plt.figure(figsize = (25,10))
ax = fig.add_subplot()
ax2 = ax.twinx()
ax.set_title('average temp and pressure in 2015-2017')
a = ax.plot(avgtemp, '-', label = 'pressure_avg')
b = ax2.plot(avgpressure, '-', label = 'pressure_avg',color="red")
ax.grid()
ax.set_xlabel("Days")
ax.set_ylabel(r"Pressure")
ax2.set_ylabel(r"Temperature")
lns = a + b
labs = [l.get_label() for l in lns]
ax2.legend(lns, labs, loc=0)
plt.show('avg_temp&pressure_2015-2017.png')
#####graph 2#####
n, bins, patches = plt.hist(pre, 'auto', facecolor = 'blue', alpha = 0.5)
plt.xlim((-0.01, 0.6))
plt.ylim((0, 30))
plt.title("precipitation in 2015-2017") 
plt.xlabel("precipitation")
plt.ylabel("days")
plt.show('precipitation_2015-2017.png')
#####graph 3#####
fig=plt.figure(figsize=(6,6))
plt.scatter(avgtemp,avgdew)
plt.grid(True)#show the grid
plt.axis("equal")#make the length of x as same as y
plt.title("relationship between temp and dew") 
plt.xlabel("averange temp")
plt.ylabel("averange dew")
plt.show('the relationship between temp and dew')
#####graph 4#####
data = [[],[],[],[],]
for a in range(2015,2018):
    for i in range(1,13):
        determine_avg = []
        determine_high = []
        determine_low = []
        for k in range(len(date)):
            if int(date[k][-4:]) == a:
                if date[k][1] != '/' and (int(date[k][0] + date[k][1])) == i:
                    determine_avg.append(int(temp_avg[k]))
                    determine_high.append(int(temp_high[k]))
                    determine_low.append(int(temp_low[k]))
                elif int(date[k][0]) == i:
                    determine_avg.append(int(temp_avg[k]))
                    determine_high.append(int(temp_high[k]))
                    determine_low.append(int(temp_low[k]))

        data[0].append([a,i])
        data[1].append(sum(determine_avg)/len(determine_avg))
        data[2].append(max(determine_high)-sum(determine_avg)/len(determine_avg))
        data[3].append(sum(determine_avg)/len(determine_avg)-min(determine_low))
        determine_avg.clear()
        determine_high.clear()
        determine_low.clear()

fig, ax = plt.subplots()
index = np.arange(len(data[0]))
bar_width = 0.35
opacity = 0.8
error_range=[data[3], data[2]]
error_attri = dict(elinewidth = 2, ecolor="y", capsize = 3)
plt.bar(index, data[1], bar_width, alpha = opacity, color = 'c', label = 'everangetemp', yerr = error_range,error_kw=error_attri)
plt.xlabel('date')
plt.ylabel('temperature')
plt.title('the temperature in 2015-2017')
plt.xticks(index + bar_width, tuple(data[0]), rotation = 90)
plt.legend()
plt.tight_layout()
plt.show()