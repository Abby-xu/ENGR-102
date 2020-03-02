# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 4bonus
# Date:		    18/09/2019

d=eval(input("please input the number of days "))
t="the output of the machine is"
if d <=10:
    p=10*d
    print(t,p)
elif 11<=d<=60:
    p=100+(d-10)*40
    print(t,p)
elif 61<=d<100:
    p=(2100-(d-60)*(d-60)/2 +40*(d-60))-0.5*(d-60)
    print(t,p)
else:
    print("the number that you give is not available")