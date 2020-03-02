# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 9b
# Date:		    30/10/2019
import csv
#####     import data from user     #####
filename = input("please write down the name that you want for saving data:")
P = float(input('please input the amount of the loan:'))
N = float(input('please input the number of month that the loan will be repaid:'))
i = float(input('please input the annual interest rate(i should be a decimal number, not a percentage):'))

#####  calculate the monthly payment  #####
J = i/12
M = P*((i/12)/(1-((1+i/12)**(-N))))
print('the monthly payment is:',M)

#####calculate the interest and remaining loan#####
headers = ['month number','total amount of interest','remaining on the loan',]
rows = [[0,0,P]]
i = 1
q = P
while i != (N+1):
    row = []
    row.append(i)
    inter = J*q
    row.append('%.2F'%inter)
    q = q - M + inter
    row.append('%.2f'%q)
    rows.append(row)
    i += 1

#####   put all data in a csv file   #####
filename = filename+'(loan is decreasing).csv'
with open(filename,'w')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

#####   calculate in another way   #####
a = P/N #calculate the loan that user has to pay for each month
headers = ['month number','total amount of interest','monthly payment','remaining on the loan',]
rows = [[0,0,0,P]]
i = 1
while i != (N+1):
    row = []
    row.append(i)
    inter = J*P
    row.append('%.2F'%inter)
    b = a + inter
    row.append('%.2F'%b)
    P -= a
    row.append('%.2F'%P)
    rows.append(row)
    i += 1

#####   put all data in a csv file   #####
filename = filename+'(loan is not decreasing).csv'
with open(filename,'w')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)