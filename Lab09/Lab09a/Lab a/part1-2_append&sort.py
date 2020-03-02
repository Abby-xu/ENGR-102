def bubble_sort(nums):

    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):   
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

'''input'''
data = []
print('Enter "stop" as your x-value to stop input of values')
while True:
    coord = []
    x = input("Enter x value: ")
    if x == "stop":
        break
    y = input("Enter y value: ")
    coord.append(int(x))
    coord.append(int(y))
    data.append(coord)
    
print(data)

'''sort data'''
data = bubble_sort(data)
print(data)

