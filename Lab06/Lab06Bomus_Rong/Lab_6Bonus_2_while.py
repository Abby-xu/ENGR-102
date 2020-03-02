# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 6b
# Date:		    03/10/2019


#define the prime number
def P(n):
    b = 2
    for b in range(2,n):
        if n%b == 0:
            return False
        elif b == n-1:
            return True
#define vailable
n = 3
num = 0
#lost 2 when define the prime
print("2 is prime")
#use loop for running from 2 to 100 
while n < 100:
    if P(n) == True:
        print(n,"is prime.")
        n += 1
        num += 1
    else:
        print(n,"is not prime.")
        n += 1

print("there are",num+1,"prime numbers between 2 and 100.")