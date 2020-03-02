import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import * #用于求导积分等科学计算
 
def draw_plot_set():#设置画图格式
    ax = plt.gca()
    #改变坐标轴位置
    ax.spines['right'].set_color('none')#删除原来轴
    ax.spines['top'].set_color('none')#删除原来轴
    ax.xaxis.set_ticks_position('bottom')#在0点处增加轴
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')#在0点处增加轴
    ax.spines['left'].set_position(('data',0))
    #设置坐标名
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.grid(True)#打开网格
 
def dif(left,right,step):#求导 左右区间以及间隔
    x,y = symbols('x y')#引入x y变量
    #expr = x*pow(E,x)#计算表达式
    expr = eval(input(''))
    x_value = [] #save x value
    y_value = [] #save x f(x) value
    y_value_int = [] #save x f(x)_dot value
    expr_int = integrate(expr,x)#求函数的不定积分  c=0
    print(integrate(expr,(x,-oo,oo)))#对x求定积分 负无穷到正无穷
    for i in np.arange(left,right,step):
        x_value.append(i)
        y_value.append(expr.subs('x',i))#将i值代入表达式
        y_value_int.append(expr_int.subs('x',i))#将i值代入积分表达式
 
    draw_plot_set()#设置画图格式
    plt.plot(x_value,y_value,"b-",linewidth=1,label='f(x)='+str(expr)) #画图
    plt.plot(x_value,y_value_int,"r-",linewidth=1,label='F(x)='+str(expr_int)) #画图
    
    plt.legend()#显示图例
    plt.show()#显示图像
    
 
 
if __name__ == '__main__':
    draw_plot_set()#设置画图格式
    dif(-30,30,0.1)