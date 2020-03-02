# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names:    Benjamin Mejia Diaz (628004466)
#           Neil Magan-Patel
#           Rong Xu (928009312)
#           Daniel Pinilla Silva
# Section:      554
# Assignment:   Lab 11a
# Date:  10/11/19
function0 = '(x-1)^2+1'
def F(x):
    y = ((x-1)**2) + 1 #this part I changed the sign to + 
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

               ## because of this function not having a root, the function is stuck in an infinity loop 
               ## test for x = 3 no output
print('The following program will use the equation\n\n',function0.center(40))
print(newton(float(input('Enter a guess for the root of the function:'))))

###############################################
function0 = '(x-1)^2-x^3'
def complx(x):
    y = (x-1)**2 - x**3 #this part I changed the sign to + 
    return y

def complx_deriv(x):
    a = 0.1
    complx_deriv = (complx(x+a)-complx(x))/a
    return complx_deriv

def complx_newton_step(x):
    new_guess = x-(complx(x) / complx_deriv(x))
    return new_guess

def newton(x):
    guesses = [x]
    difference = 1
    new_guess = 0
    while abs(difference) > (10**-6):
        new_guess = float(('{0:.7f}').format(complx_newton_step(guesses[-1])))
        guesses.append(new_guess)
        difference = guesses[guesses.index(new_guess)-1] - guesses[guesses.index(new_guess)]
        #print(difference)
    return guesses

#            testing with 32 the number of output is 16 numbers until reached to a root
#            [32.0, 21.4661717, 14.4379603, 9.7441771, 6.6029311, 4.491604, 3.0604406, 2.0760239, 1.3873138, 0.9141049,
#            0.6498738, 0.5765821, 0.5701476, 0.5698533, 0.5698408, 0.5698403]
#            testing with -32 the number of putput is 16 numbers until reached to a root.
#            
#            [-32.0, -21.1772235, -13.9560693, -9.1328391, -5.9032702, -3.7282089, -2.2430951, -1.1957289,
#            -0.402385, 0.2573456, 0.5771725, 0.5701767, 0.5698546, 0.5698409, 0.5698403]
#            
#            
#            both test guess does converged into the root
print('The following program will use the equation\n\n',function0.center(40))
print(newton(float(input('Enter a guess for the root of the function:'))))