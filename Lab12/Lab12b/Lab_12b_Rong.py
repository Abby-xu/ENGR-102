# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:      554
# Assignment:   Lab 12b
# Date:         11/11/2019
import turtle as t

def Analysis_num(a):
    '''analysis how many sets will be drew and the remain of the vertical line'''
    num_set = a // 5
    num_ind = a % 5
    return num_set, num_ind

def Draw_set():
    '''The function should draw the individual lines automatically''' 
    for j in range(4):
        t.pendown()
        t.forward(40)
        t.penup()
        t.right(90)
        t.forward(6)
        t.right(90)
        t.forward(40)
        t.left(180)
    t.left(90-53.157)
    t.pendown()
    t.forward(50)

def Draw_ind(num_ind):
    '''The function should draw the individual lines automatically'''
    for i in range(num_ind):
        t.pendown()
        t.forward(40)
        t.penup()
        t.right(90)
        t.forward(6)
        t.right(90)
        t.forward(40)
        t.left(180)

def Draw_all(num_set,num_ind):
    '''combine with the draw functions above but consider that each raw should only have 2 sets'''
    t.setup(width = 0.5,height = 1.0)
    t.penup()
    t.goto(-200,300)
    t.speed(300)
    t.left(90)
    row = num_set // 2
    row_remain = num_set % 2
    t.pensize(2)
    t.pencolor('blue')
    for i in range(row):
        Draw_set()
        t.left(180-36.843)
        t.penup()
        t.forward(40)
        t.left(90)
        t.forward(60)
        t.left(90)
        Draw_set()
        t.left(180-36.843)
        t.penup()
        t.forward(100)
        t.right(90)
        t.forward(48)
        t.right(90)
    if row_remain != 0:
        Draw_set()
        t.left(180-36.843)
        t.penup()
        t.forward(40)
        t.left(90)
        t.forward(60)
        t.left(90)
    Draw_ind(num_ind)
    t.done()
    '''
    try:
        t.bye()   
    except t.Terminator:
        pass
'''
if __name__ == '__main__':
    a = int(input('please input a number that you want to draw tally mark:'))
    num_set, num_ind = Analysis_num(a)
    Draw_all(num_set,num_ind)