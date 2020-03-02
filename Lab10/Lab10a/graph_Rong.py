import numpy as np
import matplotlib.pyplot as plt
#####graph 1#####

#####import data from numpy#####
x = y = np.arange(-4, 4, 0.1)
x, y = np.meshgrid(x,y)
print('the data for x: \n',x)
print('the data for y: \n',y)
#####make the graph#####
plt.contour(x, y, x**2 + y**2, [9])#show the line of equation
plt.axis('equal')#make the length of x as same as y
plt.title("the circle")#title
plt.xlabel("x")#the label of x
plt.ylabel("y")#the label of y
plt.show()

#####graph 2#####
data = np.random.randint(10,100,size=10)#import data from numpy
plt.barh(np.arange(data.size), data, label='pens')#show the graph
plt.legend()#show the legend
plt.title("how many pens have you lost?") #title
plt.xlabel("the number of people")#the label of x
plt.ylabel("the number of pens lost")#the label of y
plt.show()