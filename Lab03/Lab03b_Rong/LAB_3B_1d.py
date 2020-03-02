# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:	554
# Assignment:	Lab 3b
# Date:		07/09/2019

ar= int(input("input the arrival rate:"))
sr= int(input("input the service rate:"))
al=((ar**2)/(sr*(sr-ar)))
print(al)