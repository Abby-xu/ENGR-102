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
sorted_scores = []
sorted_names = []

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



def bubble_sort(nums):

    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):   
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

scores = bubble_sort(scores)

def median(nums):
    
    if len(nums) < 1:
        return None
    if len(nums)%2 == 1:
        return (nums)[len(nums)//2]
    else:
        return (nums)[len(nums)//2-1:len(nums)//2+1]/2.0

median = median(scores)

made_cut = []
n_made_cut = []
for i in range(len(scores)):
    if sorted_scores[i] >= median:
        n_made_cut.append(scores[i])

    else:
        made_cut.append(scores[i])

print("",made_cut)
print("",n_made_cut)
