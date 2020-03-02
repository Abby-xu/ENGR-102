# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 9b
# Date:		    29/10/2019
########import the package##########
import numpy as np
from matplotlib import pyplot as plt  

#######create the vector as v, and create the matrix as M#########
v = np.array([[1,0]])
print("the vector is:",v,v.shape)
M = np.matrix([[1.00583,-0.087156], [0.087156,1.00583]])
print("the matrix is:\n",M,M.shape)

##########make a loop to mutiply the vector and matrix############
print("--------------------")
a = 0
v_x = v
v_x_list = []
x = []
y = []
while a != 200:
    v_x = np.dot(v_x,M)
    print(v_x)
    x.append(v_x[0,0])
    y.append(v_x[0,1])
    a += 1
#print(x)
#print(y)

##############draw the graph#################
fig=plt.figure()
plt.plot(x, y)
plt.grid(True)#show the grid
plt.axis("equal")#make the length of x as same as y
plt.xlim((-5, 8))#show range of x
plt.ylim((-5, 8))#show domain of y
plt.title("Archimedean spiral") 
plt.xlabel("x")
plt.ylabel("y")
plt.show(fig)