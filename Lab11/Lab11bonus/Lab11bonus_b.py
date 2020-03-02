# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 10b
# Date:		    7/11/2019

def my_function_b(name,cost,value):
    net = []
    for i in range(len(name)):
        a = float(value[i]) - float(cost[i])
        net.append(a)
    def get_key(dct, value):
        return [k for (k,v) in dct.items() if v == value]
    dic = dict(map(lambda x,y:[x,y],name,net))
    b = min(net)
    c = get_key(dic, b)
    print(c)
    return c,b

if __name__ == '__main__':
    i = eval(input('please input a list of name :'))
    j = eval(input('please input a list of cost :'))
    k = eval(input('please input a list of revenue :'))
    c, b = my_function_b(i,j,k)
    print('the name of least profitable facility is(are):',c)
    print('the net prefitability of the least profitable facility is:',b)