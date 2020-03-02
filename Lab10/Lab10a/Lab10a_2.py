#as a team, we have gone through all required sections of the tutorial, and each team member understands the material.
import numpy as np
import numpy.matlib

#####print A,B,C,D######
a = np.matlib.rand((3,4))
print (a)
b = np.matlib.rand((4,2))
print (b)
c = np.matlib.rand((2,3))
print (c)
d = np.matlib.rand((3,1))
print (d)
print("-----------------")

########E = ABC#########
E = a@b@c
print(E)
print("-----------------")

########transpose#######
print(E.transpose())
print("---------------")

######solve linear system#####
x = numpy.linalg.solve(E, d)
print(x)