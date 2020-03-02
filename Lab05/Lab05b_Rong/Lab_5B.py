# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 4b
# Date:		    23/09/2019
strain=float(input("please input the number of strain:"))

if strain>0.27 or strain<0:
    print("input is invalid")
elif strain<=0.01:
    st=44/0.1*strain
    print("the stress is",st)
elif strain<=0.06:
    st=44
    print("the stress is",st)
elif strain<=0.18:
    st=44+(60-44)/(0.18-0.05)*(strain-0.05)
    print("the stress is",st)
else:
    st=60-(0.27-0.18)/10*(strain-0.18)
    print("the stress is",st)