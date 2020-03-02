# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         Esther Li 828007859
#               Dacheng Jiang 428007586
#               Rong Xu 928009312
#
# Section:		ENGR 102 554
# Assignment:	Lab 03 A
# Date:		10 September 2019

#the inputs of our mad lib: 
#   1/favorite color
#   2/name of user
#   3/hometown
#   4/name of frinend
#   5/the number of years since you meet
#   6/the gift that you gived to your frinend

a=str(input("please input the favorite color:"))
b=str(input("please input the favorite movie:"))
c=str(input("please input your hometown:"))
e=str(input("please input the gift that you gived to your friend:"))
f=float(input("please input the number of years since you met:"))

g=f*365

print(str(g)+"days ago, when I came back to"+str(c)+"to visit my parents, I saw a girl just sitting at a bus station and watching a book. It's rainy, and she didn't bring the umbrella. That's the first time I met her.\n\t I've never thought that we could be friends, but the truth is we became good friend since that met. Both of us like the"+str(b)+"and"+str(a)+"so that we had more topic to talk about. Today is her birthday, and I'd like to give"+str(e)+"to her as a gift.")