# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 6b
# Date:		    03/10/2019

#simplify
result = [ x for x in range(2,101) if 0 not in [ x%y for y in range(2,x)]]
print (result)
print("-------------")

import math
#define the prime number
def P(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i == 0):
            return False
    return True
#use loop for running from 2 to 100 
num = 0
for n in range(2,101):
    if P(n) == True:
        print(n,"is prime.")
        num += 1
    else:
        print(n,"is not prime.")
print("there are",num,"prime numbers between 2 and 100.")