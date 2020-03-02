# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 7b
# Date:		    09/10/2019

print("welcome to the game", end = '')
print('for any position you want to describe, first show which line(the number),then show which colums')
print('like, if you want to move the Q, you can input "14"')
print("if you want to exit, youcan just move a blank space")
board = [
    ['R','N','B','Q','K','B','N','R'],
    ['P','P','P','P','P','P','P','P'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['p','p','p','p','p','p','p','p'],
    ['r','n','b','q','k','b','n','r',]
]
while True:
    for i in board:
        print(i)

    a = str(input("please input the position that you want to move:"))
    b = str(input("please input the position that you want to move to:"))
    if board [int(a[0])-1] [int(a[1])-1] == '.':
        break
    board [int(b[0])-1] [int(b[1])-1] = board [int(a[0])-1] [int(a[1])-1]
    board [int(a[0])-1] [int(a[1])-1] = '.'
print("thanks fo rusing, have a good day:)")