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
#Pv=20Lg(U/0.775)(dB)
a = float(input ("Enter the number of voltage: "))
b=20*log(a)
print("The number of the voltage level(power gain): "+str(b))