# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 4b
# Date:		    17/09/2019

a=float(input("please inter the first number"))
b=float(input("please inter the second number"))
c=float(input("please inter the third number"))
e=""

if a < b or a == b: 
    e="b is the bigger number"
    if b < c or b == c:
        e="c is the biggest number" or "c is equal to b"
    else:   
        e="b is the biggest number"
else:
    e="a is the bigger number" or "a is equal to b"
    if a < c or a == c:
        e="c is the biggest number" or "c is equal to a"
    else:
            e="a is the biggest number"

print(e)