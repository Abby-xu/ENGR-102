# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:	554
# Assignment:	Lab 3b
# Date:		07/09/2019

f_nor= int(input("input the normal stress:"))
co= int(input("input the cohesion:"))
a=int(input("input the angle of internal friction:"))
θ=a*pi/180
f3=co+f_nor*tan(θ)
print(f3)