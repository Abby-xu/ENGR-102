# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 10b
# Date:		    7/11/2019

def mailing_label(n,c,s,z,a1,a2):
    if a2 == '':
        print(n,'\n'+a1,'\n'+c,s,z)
    else:
        print(n,'\n'+a1,'\n'+a2,'\n'+c,s,z)

if __name__ == '__main__':
    name = input('please input your name:')
    city = input('please input the city you live in:')
    state = input('please input the state you live in(the abbreviation):')
    zip_code = input('please input the zip code:')
    address_1 = input('please input your address(the first line):')
    address_2 = input('please input your address(the second line if you have, or nothing):')
    mailing_label(name,city,state,zip_code,address_1,address_2)