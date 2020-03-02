# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name:         RongXu
# Section:  	554
# Assignment:	Lab 10b
# Date:		    7/11/2019


def avg_speed(t,d):
    avg_speed = []
    for i in range(len(t)-1):
        avg_speed.append((float(d[i+1])-float(d[i]))/(float(t[i+1])-float(t[i])))
    return avg_speed

if __name__ == '__main__':
    t = eval(input('please input a list of time:'))
    d = eval(input('please input a list of distance'))
    print('the averange speed is:',avg_speed(t,d))
