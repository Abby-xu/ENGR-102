# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names: 	Benjamin Mejia Diaz (628004466)
# 	 		Neil Magan-Patel
# 	 		Rong Xu (928009312)
#			Daniel Pinilla Silva
# Section:		554
# Assignment:	Lab 6a
# Date:  10/04/19

scores = []
names = []

#####ask user input the data and put in two lists#####
print("This program will receive scores for an arbitrary number of participants. Input a negative number to indicate end of scores.")
while True:
    score1 = int(input("Enter round 1 score: "))
    if score1 < 0:
        break
    else:
        score2 = int(input("Enter round 2 score: "))
        name = input("Enter player name: ")
        scores.append(score1+score2)
        names.append(name)

##########sort the data##########
for i in range(len(scores) - 1):
    for j in range(len(scores) - i - 1):   
        if scores[j] > scores[j + 1]:
            scores[j], scores[j + 1] = scores[j + 1], scores[j]
            names[j], names[j + 1] = names[j + 1], names[j]
            
##########find the median#########
def median(nums):
    
    if len(nums) < 1:
        return None
    if len(nums)%2 == 1:
        return (nums)[len(nums)//2]
    else:
        return (nums)[len(nums)//2-1:len(nums)//2+1]/2.0

median = median(scores)

##########judge the name which can pass to next round##########
made_cut = []
n_made_cut = []
for i in range(len(scores)):
    if scores[i] >= median:
        n_made_cut.append(names[i])
    else:
        made_cut.append(names[i])

print(made_cut,"failed to pass to the next round")
print(n_made_cut,"passed to the next round")
