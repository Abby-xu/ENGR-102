# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:51:14 2019

@author: Neil
"""


b = 10
m = 1
while True:
    x_value = input('Please enter a x value:')
    if x_value == 'stop':
        break
    else:
        x_value = int(x_value)
        print((m * x_value) + b)
        