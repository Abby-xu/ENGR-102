# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:      554
# Assignment:   Lab 12bonus
# Date:         11/11/2019
import matplotlib.pyplot as plt 
import numpy as np

def input_data():
    '''ask user for a original function and make a list of every coefficient and power number'''
    print('example: 3*X**3+2*X**2+X+3,the highest power number is 3')
    n = int(input('please input the highest powernumber of your function:'))
    co = []
    while n != -1:
        print('the powernumber is',n)
        a = float(input('please input the coefficient number:'))
        co.append(a)
        n -= 1
    return co

def find_extr(x,y):
    '''find the local max and min while using  for loop and if statement'''
    extrma1 = []
    extrmi1 = []
    for i in range(1,(len(x)-1)):
        if y[i] >= y[i-1] and y[i] >= y[i+1]:
            extrma1.append(x[i])
            extrma1.append(y[i])
    for i in range(1,(len(x)-1)):
        if y[i] <= y[i-1] and y[i] <= y[i+1]:
            extrmi1.append(x[i])
            extrmi1.append(y[i])
    return extrma1,extrmi1

def draw(x,y,y1,y2,p_maxx,p_maxy,p_minx,p_miny):
    '''draw the graph of y, y1 and y2 and annotate the local max and local min'''
    plt.plot(x,y, 'r-',linewidth=1,label='f(x)')
    plt.plot(x,y1, 'g--',linewidth=1,label="f'(x)")
    plt.plot(x,y2, 'b-',linewidth=0.8,label="f''(x)")
    plt.annotate("local max:(%f,%f)" %(p_maxx,p_maxy), xy=(p_maxx,p_maxy), textcoords='offset points', arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate("local min:(%f,%f)" %(p_minx,p_miny), xy=(p_minx,p_miny), textcoords='offset points',arrowprops=dict(facecolor='black', shrink=0.05))
    plt.legend()
    plt.show()

if __name__ == '__main__':
    co = input_data()
    func = np.poly1d(np.array(co))
    func1 = func.deriv(m=1)
    func2 = func.deriv(m=2)
    x = np.linspace(-100,100,3000)
    y = func(x)
    y1 = func1(x)
    y2 = func2(x)
    ma,mi = find_extr(x,y)
    print('the local extrma is:',ma)
    print('the local extrmi is:',mi)
    draw(x,y,y1,y2,ma[0],ma[1],mi[0],mi[1])