# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 7b
# Date:		    09/10/2019

board = [
["R","N","B","Q","K","B","N","R"],
["P","P","P","P","P","P","P","P"],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],
["p","p","p","p","p","p","p","p"],
["r","n","b","q","k","b","n","r"]
]
print("welcome to play,if you wanna stop,you can just move a blank space")
print("for the position of each chess piece，please first input its y position,than input its x position.")
print("forexample, for the 'B' is 13 and 'k' is 85")    
while True:
    for i in board:
        print(i)
    a = input("which position are you going to move:")
    b = input("which position you wanna move to:")
    if board[(int(a[0])-1)][(int(a[1])-1)] == ".":
        break
    board[(int(b[0])-1)][(int(b[1])-1)] = board[(int(a[0])-1)][(int(a[1])-1)]
    board[(int(a[0])-1)][(int(a[1])-1)] = "."