# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         Esther Li       828007859
#               Dacheng Jiang   428007586
#               Rong Xu         928009312
#
# Section:		ENGR 102 554
# Assignment:	Lab 04 A_2
# Date:		    24 September 2019

#1)	a and b and c
#2)	a or b or c
#3)	(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
#4)	(not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))

a=1
b=1
c=1
print(bool(a and b and c))
a=1
b=0
c=1
print(bool(a and b and c))

a=1
b=1
c=1
print(bool(a or b or c))
a=0
b=0
c=0
print(bool(a or b or c))

a=1
b=0
c=1
print(bool((not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)))
a=1
b=1
c=0
print(bool(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b))

a=1
b=1
c=1
print(bool((not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))))
a=0
b=0
c=0
print(bool((not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))))