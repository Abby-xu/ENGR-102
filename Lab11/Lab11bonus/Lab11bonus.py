# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 10bonus
# Date:		    7/11/2019
import math
import pandas as pd

###############      A       ###############
def my_function_a (l,w,h,r):
    v_box = l*w*h
    v_hole = math.pi*(r**2)*h
    #assuming the hole has radius less than min(length/2, width/2) 
    if (r <= (l/2)) and (r <= (w/2)):
        remain = v_box - v_hole
    #assuming the hole has larger radius 
    else:
        remain = v_hole - v_box
    return remain

if __name__ == '__main__':
    l = float(input('please input the length of the box:'))
    w = float(input('please input the width of the box:'))
    h = float(input('please input the height of the box:'))
    r = float(input('please input the radius of the hole:'))
    print('the volume of material remaining is:',my_function_a(l,w,h,r))

###############        B        ###############
def my_function_b(name,cost,value):
    net = []
    for i in range(len(name)):
        a = float(value[i]) - float(cost[i])
        net.append(a)
    dic = dict(map(lambda x,y:[x,y],name,net))
    def get_key(dct, value):
        return [k for (k,v) in dct.items() if v == value]
    b = min(net)
    c = get_key(dic, b)
    return c,b

if __name__ == '__main__':
    i = eval(input('please input a list of name :'))
    j = eval(input('please input a list of cost :'))
    k = eval(input('please input a list of revenue :'))
    c, b = my_function_b(i,j,k)
    print('the name of least profitable facility is(are):',c)
    print('the net prefitability of the least profitable facility is:',b)

###############        C        ###############
def my_function_c(n,c,s,z,a1,a2):
    if a2 == '':
        print(n,'\n'+a1,'\n'+c,s,z)
    else:
        print(n,'\n'+a1,'\n'+a2,'\n'+c,s,z)

if __name__ == '__main__':
    name = input('please input your name:')
    city = input('please input the city you live in:')
    state = input('please input the state you live in(the abbreviation):')
    zip_code = input('please input the zip code:')
    address_1 = input('please input your address(the first line):')
    address_2 = input('please input your address(the second line if you have, or nothing):')
    my_function_c(name,city,state,zip_code,address_1,address_2)

###############        D        ###############
def my_function_d(filenamecsv):
    writename = filenamecsv[:-4]+'.tsv'
    with open(filenamecsv, 'r') as read_csv:
        csv_read = pd.read_csv(filenamecsv)
        with open(writename,'w') as write_tsv:
            write_tsv.write(csv_read.to_csv(sep = '\t'))

if __name__ == '__main__':
    filenamecsv = input('please input the name of your csv file:')
    my_function_d(filenamecsv)

###############        E        ###############
def my_function_e(l):
    a = max(l)
    b = min(l)
    c = sum(l)/len(l)
    return a, b, c

if __name__ == '__main__':
    l = eval(input('please input a list that you want to deal with:'))
    x, y, z = my_function_e(l)
    print('the max value is:',x,'\nthe min value is:',y,'\nthe mean is:',z)

###############        F        ###############
def my_function_f(t,d):
    avg_speed = []
    for i in range(len(t)-1):
        avg_speed.append((float(d[i+1])-float(d[i]))/(float(t[i+1])-float(t[i])))
    return avg_speed

if __name__ == '__main__':
    t = eval(input('please input a list of time:'))
    d = eval(input('please input a list of distance:'))
    print('the averange speed is:',my_function_f(t,d))