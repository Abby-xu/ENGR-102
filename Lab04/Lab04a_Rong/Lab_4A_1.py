# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         Esther Li            828007859
#               Dacheng Jiang        428007586
#               Rong Xu              928009312
#               Joseph Buskmiller    728007490   
#Section:		ENGR 102 554
# Assignment:	Lab 04 A_1
# Date:		    24 September 2019

a = 1/7
print(a)
b = a*7
print(b)

a = 1/7
print(a)
b = 7*a
print(b)
c = 2*a
d = 5*a
e = c+d
print(e)
# define tolerance 
TOL = 1e-10
# check if b and e are equal within specified tolerance
if abs(b-e) < TOL:
	print("b and e are equal within tolerance of", TOL)
else:
	print("b and e are NOT equal within tolerance of",TOL)


from math import *
x = sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z)
# define tolerance 
TOL = sqrt(1/3)
# check if b and e are equal within specified tolerance
if abs(y-z) < TOL:
	print("y and z are equal within tolerance of", TOL)
else:
	print("y and z are NOT equal within tolerance of",TOL)

print("-----------------------")

a=1/647387
print("the first example'a':",a)
b=a*647387
print("the first example'b':",b)
print("Is 1/647387 the same as (1/647387)*647387?",a == b)
print("the difference between these two number is:",b-a)

a = 1/48
print("the second example'a':",a)
b = 48*a
print("the second example'b':",b)
c = 36*a
d = 12*a
e = c+d
print("the second example'e':",e)
print("Is 'a' the same as 'e'?",a == e)
print("Is 'a' the same as 'b'?",a == b)
print("Is 'b' the same as 'e'?",b == e)
# define tolerance 
TOL = 1e-10
# check if b and e are equal within specified tolerance
if abs(b-e) < TOL:
	print("b and e are equal within tolerance of", TOL)
else:
	print("b and e are NOT equal within tolerance of",TOL)

from math import *
x = sqrt(1/0.001)
print("the third example'x':",x)
y = x*x*0.001
print("the third example'y':",y)
z = x*0.001*x
print("the third example'z':",z)
print("Is 'x' the same as 'y'?",x == y)
print("Is 'y' the same as 'z'?",y == z)
print("Is 'x' the same as 'z'?",x == z)
# define tolerance 
TOL = sqrt(1/48)
# check if b and e are equal within specified tolerance
if abs(y-z) < TOL:
	print("y and z are equal within tolerance of", TOL)
else:
	print("y and z are NOT equal within tolerance of",TOL)

print("-----------------")