from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from threading import Thread

# input
while True:
    data = []
    print('Enter "stop" as your x-value to stop input of values')
    while True:
        coord = []
        x = input("Enter x value: ")
        if x == "stop":
            break
        y = input("Enter y value: ")
        coord.append(eval(x))
        coord.append(eval(y))
        data.append(coord)

    print(data)

    # sort data
    data = sorted(data, key=(lambda x: x[0]))
    print(data)

    # create a list to put X and Y, then transfer to the tuple
    X = []
    Y = []

    for i in range(len(data)):
        x = (data[i][0])
        y = (data[i][1])
        X.append(x)
        Y.append(y)
    #x = [int(data[i][0])]
        #y = [int(data[i][1])]
    X = tuple(X)
    Y = tuple(Y)

    #print(X)
    #print(Y)

    #create the model
    liner = LinearRegression()
    #Fitting model
    liner.fit(np.reshape(X,(-1,1)),np.reshape(Y,(-1,1)))
    print(liner)

    #predict and graphing
    y_pred = liner.predict(np.reshape(X,(-1,1)))
    
    plt.figure(figsize=(5,5))
    plt.scatter(X,Y)
    plt.plot(X,y_pred, color="r")
    t=Thread(target=plt.show(),args=[])
    f=liner.coef_
    q=liner.intercept_
    #print(f)
    #print(q)
    data=[]
    s=input('Would you want quit,please Enter"quit"or Enter except"x":')
    if s=='quit':
        break
    print("except 'y':",f[0][0]*eval(s)+q[0])