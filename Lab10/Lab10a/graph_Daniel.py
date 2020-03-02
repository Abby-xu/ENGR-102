# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:05:02 2019

@author: pinil
"""

import numpy as np
import matplotlib.pyplot as plt

##### Scatter graph ######

#Data generation
x = np.random.rand(50)
y = np.random.rand(50)
print("x-axis data: \n", x)
print("y-axis data: \n", y)
#Plotting data
plt.scatter(x, y)
plt.title("Scatter graph")
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.show()


###### Histogram ######

#Data generation
x = np.random.randint(1, 1000, 1000)

#Plotting data
plt.hist(x, bins=200)
plt.title("Histogram")
plt.xlabel("x_axis")
plt.ylabel("y-axis")
plt.show()



 