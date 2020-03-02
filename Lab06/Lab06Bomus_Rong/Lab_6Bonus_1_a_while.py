# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 6b
# Date:		    03/10/2019

#input positive number
b = int(input("please input a positive integer:"))
#input positive number
a = 0
i = 0
#use loop
while True:
    if i < b:
        i += 1
        a = a+i
    if i == b:
        break
print("the sum of all of the numbers",a)