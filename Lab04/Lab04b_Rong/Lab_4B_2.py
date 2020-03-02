# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 4b
# Date:		    17/09/2019

from math import*
print("if there is a equation that '0=ax^2+bx+c'")
a=float(input("please input a number of a:"))
b=float(input("please input a number of b:"))
c=float(input("please input a number of c:"))
if a!=0:
    delta = b**2-4*a*c
    if delta < 0:
        print("there is no real root,but")
        root=delta**0.5
        x1=(-b+root)/(2*a)
        x2=(-b-root)/(2*a)
        print("the solutions with imaginary number are:")
        print(complex(x1))
        print(complex(x2))
        print("the real root is at:" +str(-1*b/(2*a))+" the imaginary root is at x="+str(sqrt(4*a*c-b*b)/(2*a))+"i");
    elif delta == 0:
        s = -b/(2*a)
        print("the only root is",s)
    else:
        root =sqrt(delta)
        x3=(-b+root)/(2*a)
        x4=(-b-root)/(2*a)
        print("the first solution is",x3)
        print("the second solution is",x4)
elif a==0 and b!=0:
    print("this is a linear equation with one root")
    x=-c/b
    print("the solution is:",x)
elif a==0 and b==0:
    print("there is an error with this equation")