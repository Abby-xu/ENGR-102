from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

#input
data = []
print('Enter "stop" as your x-value to stop input of values')
while True:
    coord = []
    x = input("Enter x value: ")
    if x == "stop":
        break
    y = input("Enter y value: ")
    coord.append(int(x))
    coord.append(int(y))
    data.append(coord)
    
print(data)

#sort data
data = sorted(data,key=(lambda x:x[0]))
print(data)

#create a list to put X and Y, then transfer to the tuple
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

print(X)
print(Y)

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
plt.show()
print(liner.coef_)
print(liner.intercept_)

#let user input the x value to output the y value
'''
while True:
    predict_x = input('Please enter a x value:')
    if predict_x == 'stop':
        break
    else:
        predict_x = int(predict_x)
        result = liner.predict(predict_x)
        print(result)
'''