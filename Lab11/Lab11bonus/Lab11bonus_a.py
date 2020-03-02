# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 10b
# Date:		    7/11/2019
import math

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

##### test cases #####

#test case 1 : radius less than min
'''
l = 4 // w = 6 // h = 10 // r = 1
v_box = 240
v_hole = 10*pi
v_remian = 240 - 10*pi
'''
#test case 2 : radius as same as min
'''
l = 8 // w = 8 // h = 5 // r = 4
v_box = 320
v_hole = 16*pi
v_remain = 320 - 16*pi
'''
#test case 3 : radius is lager than min
'''
l = 6 // w = 4 // h = 7 // r = 5
v_box = 168
v_hole = 25*pi
#since hole is larger than the box
v_remian = 25*pi-168
'''