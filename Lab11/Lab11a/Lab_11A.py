# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:38:17 2019

@author: pinil
"""
function0 = '(x-1)^2-1'
def F(x):
    y = ((x-1)**2)-1
    return y

def deriv(x):
    a = 0.1
    F_deriv = (F(x+a)-F(x))/a
    return F_deriv

def newton_step(x):
    new_guess = x-(F(x)/deriv(x))
    return new_guess

def newton(x):
    guesses = [x]
    difference = 1
    new_guess = 0
    while abs(difference) > (10**-6):
        new_guess = float(('{0:.7f}').format(newton_step(guesses[-1])))
        guesses.append(new_guess)
        difference = guesses[guesses.index(new_guess)-1] - guesses[guesses.index(new_guess)]
        #print(difference)
    return guesses
print('The following program will use the equation\n\n',function0.center(40))
print(newton(float(input('Enter a guess for the root of the function:'))))