# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names: 	Benjamin Mejia Diaz (628004466)
# 	 		Neil Magan-Patel
# 	 		Rong Xu(928009312)
#			Daniel Pinilla Silva
# Section:		554
# Assignment:	Lab 6a
# Date:  10/04/19

########### Test Cases ##############
'''
Test case 1 (normal case)
Input of coefficients: A = 3/B = 4/C = 5/D = 6
Input of bounds: a = 10/b = -10
Output: 
    the root is -1
    number of bisections: 26

Test case 2 (edge case)
Input of coefficients: A = 4/B = 5/C = 6/D = 7
Input of bounds: a = 8/b = -1
Output: 
    the root is "there is no root"
    number of bisections: (miss)

Test case 3 (edge case)
Input of coefficients: A = 0/B = 48/C = 53/D = 7
Input of bounds: a = /b = (miss)
Output: 
    the root is -0.9507845668542633/-15338209981240336
    number of bisections: (miss)

Test case 4 (normal case)
Input of coefficients: A = 13/B = 11/C = 7/D = 5
Input of bounds: a = -1000000000/b = 1000000000
Output: 
    the root is -0.8
    number of bisections: 52

Test case 5 (edge case)
Input of coefficients: A = 0/B = 0/C = 9/D = 18
Input of bounds: a = /b = (miss)
Output: 
    the root is -2
    number of bisections: (miss)
'''

import math as mth
#ask user input four coefficients as for function
'''
should we change the coefficients for B/C/D as floats instead of integers？
make instraction more specific, we can add some info like:
'as a function like f(x)=A*x^3+B*x^2+C*x+D'
'''
A = float(input('Enter whole number coefficient "A":'))
B = int(input('Enter whole number coefficient "B":'))
C = int(input('Enter whole number coefficient "C":'))
D = int(input('Enter whole number coefficient "D":'))

counter = 1

############# Checking for correct inputs ##################
if A==0:
    #if A=0, the function will be a quadratics
    discriminant=((C**2)-(4*B*D))
    if (B == C == 0) and (D != 0):
        print('The coefficients provided are just a constant line.')
    #if A=0 and B=0, the function will be a linear equation
    elif (B == 0):
        sing_root = (-1*D)/C
        print("The root is", sing_root)
    elif (discriminant != 0):
        if (discriminant > 0):
            root1 = ((-1*C)+(mth.sqrt(abs(discriminant))))/(2*B)
            root2 = ((-1*C)-(mth.sqrt(abs(discriminant))))/(2*B)
            print("The roots are", root1, "and", root2)
        #the roots of function have imaginary number
        elif (discriminant < 0):
            root_imag1_1 = (-1*C)/(2*B)
            root_imag1_2 = (mth.sqrt(abs(discriminant)))/(2*B)
            print("The roots are", root_imag1_1, "+", str(root_imag1_2) + "i", "and", root_imag1_1, "-", str(root_imag1_2) + "i")
    else:
        '''
        this command doesn't work anymore because this if function is in the function that
        'if A == 0',so the 'root_unique' will be 0
        '''
        root_unique=(-B)/(2*A)
        print("The root is", root_unique)
        
else:
    #ask user input upper bound and lower bound
    bound_a = int(input("Enter bound 'a' (negative):"))
    bound_b = int(input("Enter bound 'b' (positive):"))
    
############## Computing the root ##################
#define polynomial equation: AX^3 + BX^2 + CX + D
fa = (A * (bound_a ** 3)) + (B * (bound_a ** 2)) + (C * bound_a) + D
fb = (A * (bound_b ** 3)) + (B * (bound_b ** 2)) + (C * bound_b) + D
length = bound_a-bound_b
minimum = 10 ** -6
#Check that between two bounds, there is a root.
if (fa > 0 and fb < 0) or (fa < 0 and fb > 0):

    while not(abs(length) <= minimum):

        p = ((bound_a+bound_b)/2.0)
        fp = (A * (p ** 3)) + (B * (p ** 2)) + (C * p) + D

        if fa > 0 and fp < 0:
            #do the thing(redefine P and get a new polynomial)
            bound_b = p
            fb = (A * (bound_b ** 3)) + (B * (bound_b ** 2)) + (C * bound_b) + D
        elif fb > 0 and fp < 0:
            #do the thing(redefine P and get a new polynomial)
            bound_a = p
            fa = (A * (bound_a ** 3)) + (B * (bound_a ** 2)) + (C * bound_a) + D
        elif fa < 0 and fp > 0:
            #do the thing(redefine P and get a new polynomial)
            bound_b = p
            fb = (A * (bound_b ** 3)) + (B * (bound_b ** 2)) + (C * bound_b) + D
        elif fb < 0 and fp > 0:
            #do the thing(redefine P and get a new polynomial)
            bound_a = p
            fa = (A * (bound_a ** 3)) + (B * (bound_a ** 2)) + (C * bound_a) + D

        counter += 1 #add 1 to the counter for each trail to record the iterations.
        length = bound_a-bound_b #redefine the length because one of the bounds changed

    print("The root is at x =",'{:g}'.format(float('{:.1g}'.format(p))),"and it took",counter,"bisections to find it.")

#when one of the bounds that user input is root
elif fa == 0 or fb == 0:

    if fa == 0:
        print("The root is at x =",bound_a,"and it took no bisections to find it.")
    else:
        print("The root is at x =",bound_b,"and it took no bisections to find it.")

#when both of the bounds that user input cannot be used
else:

    print("There is no root between these two points on the graph.")
        