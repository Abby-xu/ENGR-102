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

#sort data
data = sorted(data,key=(lambda x:x[0]))

#create a list to put X and Y
X = []
Y = []

for i in range(len(data)):
    x = (data[i][0])
    y = (data[i][1])
    X.append(x)
    Y.append(y)

#let user input the x value to output the y value
while True:
    predict_x = input('Please enter a x value:')
    if predict_x == 'stop':
        break
    else:
        predict_x = int(predict_x)
        for i in range(len(X)):
            if predict_x < X[0]:
                result = Y[0]-(Y[1]-Y[0])/(X[1]-X[0])*(X[0]-predict_x)
                print(result)
                break
            elif predict_x > X[i] and predict_x < (X[i+1]):
                result = Y[i]+(Y[i+1]-Y[i])/(X[i+1]-X[i])*(predict_x-X[i])
                print(result)
                break
            elif predict_x == X[i]:
                result = Y[i]
                print(result)
                break
            elif predict_x > X[-1]:
                result = Y[-1]+(Y[-1]-Y[-2])/(X[-1]-X[-2])*(predict_x-X[-1])
                print(result)
                break