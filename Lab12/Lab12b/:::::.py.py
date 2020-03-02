import turtle
import math
 
tallymarks = turtle.Turtle()
#ask for input number
number = 18
tallymarks.right(90)
x = 0
for i in range(1,number+1):
  if(i%5 == 0): 
    tallymarks.right(135)
    tallymarks.forward(30*math.sqrt(2))
    tallymarks.right(225)
  else: 
    tallymarks.penup()
    tallymarks.goto(x*10,0)
    tallymarks.pendown()
    tallymarks.forward(30)
  x = x + 1
turtle.done()

'''
def Analysis_num(a):
	if a < 5:
		num_set = 0
		num_ind = a
	else:
		num_set = a // 5
		num_ind = a % 5
	return num_set, num_ind
a = int(input('please input a number that you want to draw with tally mark:'))
num_set, num_ind = Analysis_num(a)
print(num_set,num_ind)

def Draw_set(num_set):
  '''