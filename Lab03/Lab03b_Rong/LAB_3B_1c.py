# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:	554
# Assignment:	Lab 3b
# Date:		07/09/2019

ini_pro= int(input("input the initial production rate:"))
ini_dec= int(input("input the decline rate:"))
t= int(input("input the number of days:"))
h=0.8
pro=(d*ini_pro/((1+h*ini_dec*t)**(1/h)))