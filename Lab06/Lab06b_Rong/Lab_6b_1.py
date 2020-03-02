# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 6b
# Date:		    03/10/2019

#input the variables
a = float(input("please input a to form the function f(x) if f(x)=a*x^3+b*x^2+c*x+d:"))
b = float(input("please input b to form the function f(x) if f(x)=a*x^3+b*x^2+c*x+d:"))
c = float(input("please input c to form the function f(x) if f(x)=a*x^3+b*x^2+c*x+d:"))
d = float(input("please input d to form the function f(x) if f(x)=a*x^3+b*x^2+c*x+d:"))
x0 = float(input("please input x in which the value you want to get in f(x):"))

#define the function and the polynomial function
def f(x):
    return pow(x,3)*a+pow(x,2)*b+x*c+d

def df(x):
    return pow(x,2)*a*3+x*b*2+c*1

print("the the derivative polynomial is:",df(x0),"\n")

#evaluate the derivative
h = 0.1
num = 1
fx=0
while abs((f(x0+h)-f(x0))/h-(f(x0+2*h)-f(x0))/(2*h)) > pow(10,-6):
    fx=(f(x0+h)-f(x0))/h
    h = h/2
    num += 1
print("the derivative is:",fx)
print("how close that result is to the actual answer:",abs(df(x0)-(f(x0+h)-f(x0))/h))
print("the number of testing:",num,"\n")

#the first example of complex function:sin(x)
import math
h = 0.1
num = 0
d1 = (math.sin(x0+h)-math.sin(x0))/h
d2 = (math.sin(x0+2*h)-math.sin(x0))/(2*h)
while abs(d1-d2) > pow(10,-6):
    h = h/2
    num += 1
    d1 = (math.sin(x0+h)-math.sin(x0))/h
    d2 = (math.sin(x0+2*h)-math.sin(x0))/(2*h)
print("it is take",num,"times to evaluate f(x) = sin x, the derivative is",d1,"\n")

#the first example of complex function:cos(x)
import math
h = 0.1
num = 0
d1 = (math.cos(x0+h)-math.cos(x0))/h
d2 = (math.cos(x0+2*h)-math.cos(x0))/(2*h)
while abs(d1-d2) > pow(10,-6):
    h = h/2
    num += 1
    d1 = (math.cos(x0+h)-math.cos(x0))/h
    d2 = (math.cos(x0+2*h)-math.cos(x0))/(2*h)
print("it is take",num,"times to evaluate f(x) = cos x, the derivative is",d1,"\n")

#the first example of complex function:tan(x)
import math
h = 0.1
num = 0
d1 = (math.tan(x0+h)-math.tan(x0))/h
d2 = (math.tan(x0+2*h)-math.tan(x0))/(2*h)
while abs(d1-d2) > pow(10,-6):
    h = h/2
    num += 1
    d1 = (math.tan(x0+h)-math.tan(x0))/h
    d2 = (math.tan(x0+2*h)-math.tan(x0))/(2*h)
print("it is take",num,"times to evaluate f(x) = tan x, the derivative is",d1,"\n")

#the first example of complex function:x**48
h = 0.1
num = 0
d1 = (pow((x0+h),48)-pow(x0,48))/h
d2 = (pow((x0+2*h),48)-pow(x0,48))/(2*h)
while abs(d1-d2) > pow(10,-6):
    h = h/2
    num += 1
    d1 = (pow((x0+h),48)-pow(x0,48))/h
    d2 = (pow((x0+2*h),48)-pow(x0,48))/(2*h)
print("it is take",num,"times to evaluate f(x) = x**48, the derivative is",d1,"\n")