# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 6b
# Date:		    03/10/2019

#ask user inout a integer
a = int(input("please input a positive integer:"))  
num = 1
#make sure the integer that user input is even or odd
#calculate and print out each result
while a != 1:
    if a%2 == 0:
        a = a/2
        num += 1
        print(int(a))
    elif a%2 == 1:
        a = a*3+1
        num += 1
        print(int(a))
#print out the result including the times
print("it takes",num,"times to reach to 1.")