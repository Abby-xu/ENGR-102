# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names: 	Benjamin Mejia Diaz (628004466)
# 	 		Neil Magan-Patel
# 	 		Rong Xu(928009312)
#			Daniel Pinilla Silva
# Section:		554
# Assignment:	Lab 6a
# Date:  10/04/19

increasing = 0
decreasing = 0
maxintv = 0 
widgetlist = []
############## Setting up list ##############

while True:
    produced = int(input("How many widgets during day?"))
    if produced < 0:
        break
    else:
        widgetlist.append(produced)

############## Computing intervals ##############
maxintv = len(widgetlist)
for i in range(1,maxintv):
    j = 0
    incr = 0
    decr = 0
    count = 0
    while j+i < len(widgetlist):
        if widgetlist[j] > widgetlist[j+i]:
            decr +=1
        elif widgetlist[j] < widgetlist[j+i]:
            incr +=1
        count +=1
        j += 1
    incr /= count
    decr /= count
    print('\nFor ' + str(i) + '-day intervals {0:.2f}% were increasing and {1:.2f}% were decreasing'.format((incr*100),(decr*100)))