'''
This is the template file for the In Class Coding Exam
Name: Rong Xu
UIN: 928009312
Date: November 21, 2019
    
Aggie Code of Honor:
By uploading this file to eCampus,
I pledge that I have neither given nor received aid in completing this exam. In addition, 
I have followed the strictures of the Texas A&M University Aggie Honor Code during today's test period.
'''
# CODE PROVIDED - DO NOT CHANGE - Run to see INPUTS & OUTPUTS before you code
# Reading test_data.txt and CONVERTing to Float VARIABLEs: INPUTS & OUTPUTS

INPUTS = []
OUTPUTS = []
fileID = open("test_data.csv",'r')
LineI = fileID.readline()

while LineI !="":
    LineI = fileID.readline()
    if LineI !="":
        Values = LineI.rstrip('\n').split(',')
        try:
            INPUTS.append(float(Values[0]))
        except ValueError:
            continue
        try:
            OUTPUTS.append(float(Values[1]))
        except ValueError:
            continue
fileID.close()
print("INPUTS = ", INPUTS)
print("OUTPUTS = ", OUTPUTS)

# ------------------------ YOUR SOLUTION BELOW THIS LINE ---------------------------
# Part 1. Write Custom_Function here (50%)
import math as m
def Custom_Function(num):
    if num < 0:
        result = m.cos(num)
    elif num == 0:
        result = 0
    else:
        a = m.sin(num)
        result = a**2
    return result
# Part 2. Write code to test your function by calling it for every value in INPUTS (50%)
# (one at a time) and compare it to the corresponding values in OUTPUTS. 
# Print number of sucesses to console - HINT: OUTPUTS in file should match your function outputs
act_output = []
for i in range(len(INPUTS)):
    result = Custom_Function(INPUTS[i])
    act_output.append(result)
print(act_output)

right_num = 0
for i in range(len(act_output)):
    if abs(act_output[i] - OUTPUTS[i]) < (10**(-3)):
        right_num += 1

success_percent = int(right_num / (len(act_output)) * 100)
print('Success = '+str(success_percent)+'%')

# Part 3. Bonus (50% over 100%)
# Plot INPUST Vs OUTPUTS and Label Axis & put Title 
# Use matplotlib
import matplotlib.pyplot as plt 
plt.plot(INPUTS,OUTPUTS,'b-',label = 'input,output')
plt.title("INPUTS Vs OUTPUTS")
plt.scatter(INPUTS,act_output,label = 'input,act_output')
plt.xlabel("INPUTS")
plt.ylabel("OUTPUTS")
plt.legend()
plt.show()





    