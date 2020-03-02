# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Ryan Keener 228005736
#               Esther Li 828007859
#               Dacheng Jiang 428007586
#               Rong Xu 928009312
#
# Section:		ENGR 102 554
# Assignment:	Lab 02 A
# Date:		3 September 2019

from math import *

time1 = 30
time2 = 45
time3 = 37
time4 = 1200

time1 = time1 % 60
time1 -= 30

time1 = (37.667 * time1 + 50)

print("Time at 30 Seconds:")
print(time1)


time2 %= 60

time2 -= 30

time2 = (37.667*time2 + 50)

print("Time at 45 Seconds:")
print(time2)

time3 %= 60

time3 -= 30

time3 = (37.667*time3 + 50)

print("Time at 37 Seconds:")
print(time3)

time4 %= 60

time4 -= 30

time4 = (37.667*time4 + 50)

time4 += 3140

print("Time at 20 Minutes:")
print(time4)