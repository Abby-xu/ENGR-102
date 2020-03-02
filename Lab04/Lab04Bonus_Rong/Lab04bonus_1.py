# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 4bonus
# Date:		    18/09/2019

V=float(input("please input the number of characteristic of the flow:"))
d=float(input("please input the number of pipe diameter:"))
v=float(input ("please input the number of fluid kinematic viscosity:"))
Re=V*d/v
if Re < 2300:
    print("the flow is laminar, and the Re is",Re)
elif Re > 2900:
    print("the flow is turbulent, and the Re is",Re)
else:
    print("the flow is in transition, and the Re is",Re)