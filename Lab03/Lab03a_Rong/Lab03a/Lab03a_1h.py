# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         Esther Li 828007859
#               Dacheng Jiang 428007586
#               Rong Xu 928009312
#
# Section:		ENGR 102 554
# Assignment:	Lab 03 A
# Date:		10 September 2019

from math import *

a = float(input ("Enter the number of one Richter scale value: "))
b = float(input ("Enter the number of other Richter scale value : "))
#
c=10**(4.8+1.5*(a+b))
print("The differences in two Richter scale values to the ratio of energy released in two earthquakes is: "+str(c))