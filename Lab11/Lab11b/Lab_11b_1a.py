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

####### define read the csv file ######
def readfile(filename):
    dat_array = np.loadtxt(filename)
    dat = dat_array.tolist()
    data = []
    for i in range(len(dat)):
        coord = []
        coord.append(dat[i][0])
        coord.append(dat[i][1])
        data.append(coord)
    data = sorted(data,key=(lambda x:x[0]))
    return data
####### define make X and Y list ######
def find_xy(a):
    X = []
    Y = []

    for i in range(len(a)):
        x = (a[i][0])
        y = (a[i][1])
        X.append(x)
        Y.append(y)
    return X,Y
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
########## main part ##########
if __name__ == '__main__':
    filenameforread = input('please input the name of file for reading data:')
    data = readfile(filenameforread)
    print(data)
    a,b = find_xy(data)
    c = 0.0
    rows = []
    while True:
        row = []
        c = input('please input the number that you want to predict,input"stop" to stop input and return the file of prediction:')
        if c != 'stop':
            d = interpolation(c,a,b)
            row.append(float(c))
            row.append(d)
            rows.append(row)
            print('the predict point is:',row)
        else:
            break

########## write the file ##########
    '''
    filenameforwrite = input('please input the name of file for writing data:')
    filename_w = filenameforwrite + '.csv'
    headers = ['input number','predict number']
    with open(filename_w,'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)
    '''