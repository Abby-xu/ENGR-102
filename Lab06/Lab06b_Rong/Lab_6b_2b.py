# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 6b
# Date:		    03/10/2019
import math as m
sum = 0.0
num = 0
a = 0
min = m.inf
max = 0
while True:
    a = float(input("please input the number in your data:"))
    num += 1
    if a >= 0:
        if a >= max:
            max = a
        if a <= min:
            min = a
        sum = sum+a
    else:
        break
print("the sum of your data is:",sum)
print("the average number is:",sum/(num-1))
print("the maximum number is:",max)
print("the mimimum number is:",min) 