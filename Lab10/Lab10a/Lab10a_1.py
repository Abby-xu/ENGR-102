# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names: 	Benjamin Mejia Diaz (628004466)
# 	 		Neil Magan-Patel
# 	 		Rong Xu (928009312)
#			Daniel Pinilla Silva
# Section:		554
# Assignment:	Lab 8a
# Date:  10/29/19

Celsius_read = open('Celsius.dat', 'r')
Fahrenheit_write = open('Fahrenheit.dat', 'w')
for eachline in Celsius_read:
    value = "{0:.2f}".format((9 / 5) * float(eachline.strip()) + 32) + "\n"
    Fahrenheit_write.write(value)

Fahrenheit_write.close()
Celsius_read.close()

