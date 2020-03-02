import os
import numpy as np
from scipy import log
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math
from sklearn.metrics import r2_score
# 字体
plt.rcParams['font.sans-serif']=['SimHei']
 
# 拟合函数
def func(x, a, b):
#  y = a * log(x) + b
  y = x/(a*x+b)
  return y
 
# 拟合的坐标点
def bubble_sort(nums):

    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):   
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

'''input'''
data = []
print('Enter "stop" as your x-value to stop input of values')
while True:
    coord = []
    x = input("Enter x value: ")
    if x == "stop":
        break
    y = input("Enter y value: ")
    coord.append(int(x))
    coord.append(int(y))
    data.append(coord)
    
print(data)

'''sort data'''
data = bubble_sort(data)
print(data)

# 拟合函数
def func(x, a, b):
  y = a * log(x) + b
#  y = x/(a*x+b)
  return y

x0 = []
y0 = []
for i in range(len(data)):
    x0.append(data[i][0])
    y0.append(data[i][1])

print(x0)
print(y0)
 
# 拟合，可选择不同的method
result = curve_fit(func, x0, y0,method='trf')
a, b = result[0] 
 
# 绘制拟合曲线用
x1 = np.arange(2, 48, 0.1) 
#y1 = a * log(x1) + b
y1 = x1/(a*x1+b)
 
x0 = np.array(x0)
y0 = np.array(y0)
# 计算r2
y2 = x0/(a*x0+b)
#y2 = a * log(x0) + b
r2 = r2_score(y0, y2)  
 
#plt.figure(figsize=(7.5, 5)) 
# 坐标字体大小
plt.tick_params(labelsize=11) 
 # 原数据散点
plt.scatter(x0,y0,s=30,marker='o')
 
# 横纵坐标起止
plt.xlim((0, 50))
plt.ylim((0, round(max(y0))+2))
 
# 拟合曲线
plt.plot(x1, y1, "blue") 
plt.title("标题",fontsize=13) 
plt.xlabel('X（h）',fontsize=12) 
plt.ylabel('Y（%）',fontsize=12) 
 
# 指定点，y=9时求x
p = round(9*b/(1-9*a),2)
#p = b/(math.log(9/a))
p = round(p, 2)
# 显示坐标点
plt.scatter(p,9,s=20,marker='x')
# 显示坐标点横线、竖线
plt.vlines(p, 0, 9, colors = "c", linestyles = "dashed")
plt.hlines(9, 0, p, colors = "c", linestyles = "dashed")
# 显示坐标点坐标值
plt.text(p, 9, (float('%.2f'% p),9),ha='left', va='top', fontsize=11)
# 显示公式
m = round(max(y0)/10,1)
print(m)
plt.text(48, m, 'y= x/('+str(round(a,2))+'*x+'+str(round(b,2))+')', ha='right',fontsize=12) 
plt.text(48, m, r'$R^2=$'+str(round(r2,3)), ha='right', va='top',fontsize=12) 
 
# True 显示网格 
# linestyle 设置线显示的类型(一共四种) 
# color 设置网格的颜色 
# linewidth 设置网格的宽度  
plt.grid(True, linestyle = "--", color = "g", linewidth = "0.5")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x=[[400],[450],[484],[500],[510],[525],[540],[549],[558],[590],[610],[640],[680],[750],[900]]
y=[[80],[89],[92],[102],[121],[160],[180],[189],[199],[203],[247],[250],[259],[289],[356]]
plt.plot(x,y,'ks')
end=[[0],[0]]
for i in range(len(x)):
    x[i].insert(0,1)
x=np.mat(x)#转成矩阵
y=np.mat(y)
end=np.mat([0,0])
end=end.T#矩阵转逆
end=(x.T*x).I*x.T*y
end=end.getA().tolist()#矩阵转成列表
print(end)
X=[400,900]
Y=[]
Y.append(end[0][0]+end[1][0]*X[0])
Y.append(end[0][0]+end[1][0]*X[1])
plt.plot(X,Y,'g-')
plt.show()