# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:	554
# Assignment:	Lab 2b
# Date:		05/09/2019
t1=13
t2=84
t3=50
X1=1
Y1=3
Z1=7
X2=23
Y2=-5
Z2=10

V_x=(X2-X1)/(t2-t1)
D_x=V_x*(t3-t1)+X1

V_y=(Y2-Y1)/(t2-t1)
D_y=V_y*(t3-t1)+Y1

V_z=(Z2-Z1)/(t2-t1)
D_z=V_z*(t3-t1)+Z1

print("the position at time 50 is")
print(D_x,D_y,D_z)

print("--------------")

t1=13
t2=84
t3=51
X1=1
Y1=3
Z1=7
X2=23
Y2=-5
Z2=10

V_x=(X2-X1)/(t2-t1)
D_x=V_x*(t3-t1)+X1

V_y=(Y2-Y1)/(t2-t1)
D_y=V_y*(t3-t1)+Y1

V_z=(Z2-Z1)/(t2-t1)
D_z=V_z*(t3-t1)+Z1

print("the position at time 51 is")
print(D_x,D_y,D_z)

print("--------------")

t1=13
t2=84
t3=52
X1=1
Y1=3
Z1=7
X2=23
Y2=-5
Z2=10

V_x=(X2-X1)/(t2-t1)
D_x=V_x*(t3-t1)+X1

V_y=(Y2-Y1)/(t2-t1)
D_y=V_y*(t3-t1)+Y1

V_z=(Z2-Z1)/(t2-t1)
D_z=V_z*(t3-t1)+Z1

print("the position at time 52 is")
print(D_x,D_y,D_z)

print("--------------")

t1=13
t2=84
t3=53
X1=1
Y1=3
Z1=7
X2=23
Y2=-5
Z2=10

V_x=(X2-X1)/(t2-t1)
D_x=V_x*(t3-t1)+X1

V_y=(Y2-Y1)/(t2-t1)
D_y=V_y*(t3-t1)+Y1

V_z=(Z2-Z1)/(t2-t1)
D_z=V_z*(t3-t1)+Z1

print("the position at time 53 is")
print(D_x,D_y,D_z)

print("--------------")

t1=13
t2=84
t3=54
X1=1
Y1=3
Z1=7
X2=23
Y2=-5
Z2=10

V_x=(X2-X1)/(t2-t1)
D_x=V_x*(t3-t1)+X1

V_y=(Y2-Y1)/(t2-t1)
D_y=V_y*(t3-t1)+Y1

V_z=(Z2-Z1)/(t2-t1)
D_z=V_z*(t3-t1)+Z1

print("the position at time 54 is")
print(D_x,D_y,D_z)

print("--------------")

t1=13
t2=84
t3=50
t4=20
t5=50
X1=1
Y1=3
Z1=7
X2=23
Y2=-5
Z2=10
t=(t5-t4)/6

V_x=(X2-X1)/(t2-t1)
D_x5=V_x*(t3-t1)+X1
V_y=(Y2-Y1)/(t2-t1)
D_y5=V_y*(t3-t1)+Y1
V_z=(Z2-Z1)/(t2-t1)
D_z5=V_z*(t3-t1)+Z1

D_x4=D_x5-V_x*(t5-t4)
D_y4=D_y5-V_y*(t5-t4)
D_z4=D_z5-V_z*(t5-t4)

import random
R=random.randint(1,5)
t6=20+R*t
D_x6=V_x*t6
D_y6=V_y*t6
D_z6=V_z*t6

print("one of the interpolation is")
print(D_x6,D_y6,D_z6)