# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:      554
# Assignment:   Lab 12bonus
# Date:         16/11/2019
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
    start = float(input('please input the start point of the range:'))
    end = float(input('please input the end point of the range:'))
    return co, start, end

def riemann_sum_left(func, start, end ):
    '''calculate the sum of area by inputting the function, start point and end point (left point)'''
    n = 10
    num = 0
    while True:
        #x_n = np.linspace(start, end, n)
        dn = (end - start) / n
        sumFun_f = 0
        sumFun_l = 0
        for i in range(n):
            sumFun_f += func(start + i*dn )*dn
        for i in range(2*n):
            sumFun_l += func(start + 0.5*i*dn)*0.5*dn
        c = abs(sumFun_l - sumFun_f)
        if c >= (10**(-6)):
            num += 1
            n *= 2
            continue
        else:
            break
    return num, sumFun_l

def riemann_sum_right(func, start, end):
    '''calculate the sum of area by inputting the function, start point and end point (right point)'''
    n = 10
    num = 0
    while True:
        dn = (end - start) / n
        sumFun_f = 0
        sumFun_l = 0
        for i in range(n):
            sumFun_f += func(start + (i+1)*dn )*dn
        for i in range(2*n):
            sumFun_l += func(start + 0.5*(i+1)*dn)*0.5*dn
        c = abs(sumFun_l - sumFun_f)
        if c >= (10**(-6)):
            num += 1
            n *= 2
            continue
        else:
            break
    return num, sumFun_l

def riemann_sum_mid(func, start, end):
    '''calculate the sum of area by inputting the function, start point and end point (midpoint)'''
    n = 10
    num = 0
    while True:
        dn = (end - start) / n
        sumFun_f = 0
        sumFun_l = 0
        for i in range(n):
            sumFun_f += func(start + (i+1)/2*dn )*dn
        for i in range(2*n):
            sumFun_l += func(start + 0.5*(i+1)/2*dn)*0.5*dn
        c = abs(sumFun_l - sumFun_f)
        if c >= (10**(-6)):
            num += 1
            n *= 2
            continue
        else:
            break
    return num, sumFun_l

def riemann_sum_tra(func, start, end):
    '''calculate the sum of area by inputting the function, start point and end point'''
    n = 10
    num = 0
    while True:
        dn = (end - start) / n
        sumFun_f = 0
        sumFun_l = 0
        for i in range(n):
            sumFun_f += func(start + i*dn) + func(start + (i+1)*dn)*dn/2
        for i in range(2*n):
            sumFun_l += func(start + 0.5*i*dn) + func(start + 0.5*(i+1)*dn)*0.5*dn/2
        c = abs(sumFun_l - sumFun_f)
        if c >= (10**(-6)):
            num += 1
            n *= 2
            continue
        else:
            break
    return num, sumFun_l

if __name__ == '__main__':
    co, start, end = input_data()
    func = np.poly1d(np.array(co))
    num_l, sumFun_l_l = riemann_sum_left(func, start, end)
    num_r, sumFun_l_r = riemann_sum_right(func,start, end)
    num_m, sumFun_l_m = riemann_sum_mid(func,start, end)
    num_t, sumFun_l_t = riemann_sum_tra(func,start, end)
    print('it takes'+str(num_l)+'times to test and the result of left-end point is:',sumFun_l_l)
    print('it takes'+str(num_r)+'times to test and the result of right-end point is:',sumFun_l_r)
    print('it takes'+str(num_m)+'times to test and the result of right-end point is:',sumFun_l_m)
    print('it takes'+str(num_t)+'times to test and the result of trapezium point is:',sumFun_l_t)