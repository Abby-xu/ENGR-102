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
        

while scores:
    minimum = scores[0]  
    for i in scores: 
        if i < minimum:
            minimum = i
    sorted_scores.append(minimum)
    sorted_names.append(names[scores.index(minimum)])
    names.remove(names[scores.index(minimum)])
    scores.remove(minimum)  

from statistics import *
median = median(sorted_scores)

print("Median: ", median)

good_scores = []
good_names = []
bad_scores = []
bad_names = []
a = 0
for x in sorted_scores:
    if x >= median:
        good_scores.append(x)
        good_names.append(sorted_names[sorted_scores.index(x)+a])
        a += 1
    else:
        bad_scores.append(x)
        bad_names.append(sorted_names[sorted_scores.index(x)])
        
print(good_names, "passed to the next round with scores of", good_scores, "respectively.")
print(bad_names, "failed to pass to the next round with scores of", bad_scores, "respectively.")
