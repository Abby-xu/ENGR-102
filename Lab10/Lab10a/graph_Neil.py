import matplotlib.pyplot as plt
##################       piechart      ##############

size = [20,40,10,10]
labels = ['Blueberries','Orange','Banana','Apple']
print(size,'Data sets',)
print(labels,'Fruits')
plt.pie(size,labels=labels,autopct='%1.1f%%',)
plt.title('Pie Chart of fruits')
plt.show()

    
##################       Bar chart      ##############
x = [1,2,3,4,5,6,7,8]
y = [21,20,12,15,32,54,12,14]

plt.bar(x,y)
plt.title('Bar chart with random numbers')
plt.xlabel('group number')
plt.ylabel('voted yes for icecream')
print(x,'group number')
print(y,'people in the group number who voted yes')
plt.show()
###############






