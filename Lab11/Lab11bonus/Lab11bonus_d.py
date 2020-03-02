# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 10b
# Date:		    7/11/2019
import pandas as pd

def transfer(filenamecsv):
    writename = filenamecsv[:-4]+'.tsv'
    with open(filenamecsv, 'r') as read_csv:
        csv_read = pd.read_csv(filenamecsv)
        with open(writename,'w') as write_tsv:
            write_tsv.write(csv_read.to_csv(sep = '\t'))

if __name__ == '__main__':
    filenamecsv = input('please input the name of your csv file:')
    transfer(filenamecsv)