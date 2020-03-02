# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 10b
# Date:		    7/11/2019
import numpy as np
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

####### define read the csv file ######
def readfile(filename):
    dat_array = np.loadtxt(filename)
    dat = dat_array.tolist()
    data = sorted(dat,key=(lambda x:x[0]))
    
    return data
####### define interpolation #######
def interpolation(predict_x,X,Y):
    predict_x = float(predict_x)
    for i in range(len(X)):
        if predict_x < X[0]:
            result = Y[0]-(Y[1]-Y[0])/(X[1]-X[0])*(X[0]-predict_x)
            return result
            break
        elif predict_x > X[i] and predict_x < (X[i+1]):
            result = Y[i]+(Y[i+1]-Y[i])/(X[i+1]-X[i])*(predict_x-X[i])
            return result
            break
        elif predict_x == X[i]:
            result = Y[i]
            return result
            break
        elif predict_x > X[-1]:
            result = Y[-1]+(Y[-1]-Y[-2])/(X[-1]-X[-2])*(predict_x-X[-1])
            return result
            break
######## main part of program ########
if __name__ == '__main__':
    filenameforread = input('please input the name of file for reading data:')
    n = int(input('please input the number of demensions:'))
    data = readfile(filenameforread)
    c = 0.0
    rows = []
    while True:
        c = input('please input the number that you want to predict,input"stop" to stop input and return the file of prediction:')
        if c != 'stop':
            row = []                
            row.append(float(c))         
            i = 1
            while i != n: #make while loop for n dimension
                X = []
                Y = []                
                for j in range(len(data)):
                    x = (data[j][0])
                    y = (data[j][i])
                    X.append(x)
                    Y.append(y)
                d = interpolation(c,X,Y)
                row.append(d)        
                i += 1
            rows.append(row)
            print('the predict point is:',row)
        else:
            break
######### write the csv file ##########
    '''
    filenameforwrite = input('please input the name of file for writing data:')
    filename_w = filenameforwrite + '.csv'
    headers = ['input number','predict number']
    with open(filename_w,'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)
    '''
########## graphing for 3D ##########

dat = [[],[],[]]
for j in range(len(data)):
    dat[0].append(data[j][0])
    dat[1].append(data[j][1])
    dat[2].append(data[j][2])
i, j, k = dat[0], dat[1], dat[2]
data = [[],[],[]]
for a in range(len(rows)):
    data[0].append(rows[a][0])
    data[1].append(rows[a][1])
    data[2].append(rows[a][2])
x, y, z = data[0], data[1], data[2]
ax = plt.subplot(111, projection='3d')
ax.scatter(i, j, k, c = 'g')
ax.scatter(x, y, z, c = 'r')
ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()
