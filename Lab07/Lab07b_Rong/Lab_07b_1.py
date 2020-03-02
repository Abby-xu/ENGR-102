# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 7b
# Date:		    09/10/2019

word = ""
while True:
    word = input("please input a word(if you wanna stop, just input 'stop'):")
    word = word.lower()
    if word != "stop":
        if word[0] in 'aeiouy':
            word += "yay"
            print(word)
        else:
            first = word[0]
            word += first+"ay"
            word = word[1:len(word)]
            print(word)
    else:
        break