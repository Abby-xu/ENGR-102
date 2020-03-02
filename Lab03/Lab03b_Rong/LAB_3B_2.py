# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:	554
# Assignment:	Lab 3b
# Date:		07/09/2019
from math import*
print("Please give me the observer point and two vectors a and b as the two observed points")

o1= float(input("input the o1:"))
o2= float(input("input the o2:"))
o3= float(input("input the o3:"))

a1= float(input("input the a1:"))-o1
a2= float(input("input the a2:"))-o2
a3= float(input("input the a3:"))-o3

b1= float(input("input the b1:"))-o1
b2= float(input("input the b2:"))-o2
b3= float(input("input the b3:"))-o3

c=a1*b1+a2*b2+a3*b3
d=(a1**2+a2**2+a3**2)**0.5
e=(b1**2+b2**2+b3**2)**0.5
#acos(c)/d*e
θ=acos(c/(d*e))
print("the degree is")
print(θ*180/pi)