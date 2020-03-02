# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 7b
# Date:		    09/10/2019


import math as m
import numpy as n
dimension =int(input("enter the dimension that you would like to calculate:"))#ask user for dimension
x = []#the list stores first vector
for i in range(0,dimension):
    a = float(input("enter the number for the first vector:"))
    x.append(a)
#print(x)

y = []#the list stores second vector
for j in range(0,dimension):
    b = float(input("enter the number for the second vector:"))
    y.append(b)
#print(y)

sum_x = 0
for i in range(len(x)-1):
    sum_x += pow(x[i],2)
magnitude_x = m.sqrt(sum_x)
sum_y = 0
for j in range(len(y)-1):
    sum_y += pow(y[i],2)
magnitude_y = m.sqrt(sum_y)
print("the magnitude of the first vector is",magnitude_x)
print("the magnitude of the second vector is",magnitude_y)

x_array = n.array(x)
y_array = n.array(y)
a_array = x_array + y_array
b_array = x_array - y_array
print("A+B:",a_array)
print("A-B:",b_array)

sum = 0
for i in range(len(x)-1):
    sum += x[i]*y[i]
print("the dot product of two vectors is",sum)