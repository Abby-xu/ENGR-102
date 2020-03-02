# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 10b
# Date:		    7/11/2019

#Write a single function that takes in a list and returns the minimum, mean, and maximum value from the list. 

def sta(l):
    a = max(l)
    b = min(l)
    c = sum(l)/len(l)
    return a, b, c

if __name__ == '__main__':
    l = eval(input('please input a list that you want to deal with:'))
    x, y, z = sta(l)
    print('the max value is:',x,'\nthe min value is:',y,'\nthe mean is:',z)