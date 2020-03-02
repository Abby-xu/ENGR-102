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
# Date:  10/26/19

############## Compiling Data Points ##############
data = []
print('This program asks for different points, and approximates the value of any x value based on the closests points. It will only work on functions.\n\n')
print('Enter "stop" as your x-value to stop input of values.\n')
while True:
    coord = []
    x = input("Enter x value: ")
    if x == "stop":
        break
    y = input("Enter y value: ")
    coord.append(int(x))
    coord.append(int(y))
    data.append(coord)
    
###print(data)
    
############## Sorting the data ##############
def bubble_sort(nums):

    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):   
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums
data = bubble_sort(data)


############## Finding the y-value ##############
while True:
    unknown = input('Enter the x-value that is to be approximated:')
    if unknown != 'stop':
        unknown = int(unknown)
        ## This is for any point outside the given range of values = extrapolation
        if (unknown < data[0][0]) or (unknown > data[len(data)-1][0]):
            
            m = (data[len(data)-1][1]-data[0][1])/(data[len(data)-1][0]-data[0][0])
            b = data[0][1]-(m*data[0][0])
            print("{0:.2f}".format((m*unknown)+b))
        else:
        ## This is for any point inside the given range of values = intrapolation
            left = 0
            right = 0
            distance_r = float('inf')
            distance_l = float('inf')
            for i in range(len(data)):
                
                ##The ifs check for the left and right and the distance to the number all based on the x position.
                if unknown == data[i][0]:
                    ##print(data[i][1])
                    break
                if unknown > data[i][0] and abs(unknown-data[i][0]) < distance_r:
                    left = i
                    distance_r = abs(unknown-data[i][0])
                if unknown < data[i][0] and abs(unknown-data[i][0]) < distance_l:
                    right = i
                    distance_l = abs(unknown-data[i][0])
            #print(left,right)
            m = (data[right][1]-data[left][1])/(data[right][0]-data[left][0])
            b = data[left][1]-(m*data[left][0])
            print("{0:.3f}".format((m*unknown)+b))
    else:
        break