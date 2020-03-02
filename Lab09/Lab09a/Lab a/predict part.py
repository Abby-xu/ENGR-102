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