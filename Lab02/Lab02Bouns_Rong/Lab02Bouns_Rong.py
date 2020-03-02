# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:	554
# Assignment:	Lab 2b
# Date:		06/09/2019
from math import*
print("This shows the evaluation of 5*x/(x-2)evaluated close to x=1")
print("my guess is -3.0")

for x in range(0,7):
    print("the value of function1 is{}".format(sin(0.1**x)/0.1**x))

print("---------")

for x in range(0,7):
    print("the value of function2 is{}".format((1-cos(0.1**x))/((0.1**x)**2)))

print("---------")

for x in range(0,7):
    print("the value of function3 is{}".format((1+1/(10**x))**(10**x)))