# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 9b
# Date:		    29/10/2019
########import the package##########
import numpy as np
from matplotlib import pyplot as plt  
import csv

weatherdata = []
date = []
temp_avg = []
pressure_avg = []
weather_data = open('/Users/abby/Desktop/ENGR102_554/Lab10/Lab10b/WeatherDataMac.csv', 'r')
'''
with open(WeatherDataMac_file) as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    data_header = next(csv_reader)  # 读取第一行每一列的标题
    for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
        weather_data.append(row)
print(weatherdata)
'''
for eachline in weather_data:
    value_date = eachline[0,7]
    print(value_date)
    
    value_temp = 0
    value_pressure = 0
    date.append(value_date)
    temp_avg.append(value_temp)
    pressure_avg.append(value_pressure)
'''
    

weather_data.close()
