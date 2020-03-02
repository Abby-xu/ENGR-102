# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 7b
# Date:		    09/10/2019

print("this is the register part")
a = int(input("how many sets of usernames and passwords do you want to input?\n"))
users = {}
for i in range(a):
    names = str(input("please input the username:"))
    passwords = str(input("please input the password:"))
    users[names] = passwords

print("now you can login to your account")
name = str(input("please input your username:"))
if name in users:
    password = str(input("please input your password:"))
    
    while True:
        if password == users[name]:
            print("ok, you've already login!")
            break
        elif password != users[name]:
            password = str(input("sorry, your password is wrong, please input again:"))
            
        
print("thanks for using:)")