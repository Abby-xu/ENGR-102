# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         Esther Li       828007859
#               Dacheng Jiang   428007586
#               Rong Xu         928009312
#               Joseph Buskmiller 628007094
#
# Section:      ENGR 102 554
# Assignment:   Lab 05 A
# Date:         24 September 2019

#splash message
print("Heart Disease Risk Calculator.")
print("Please enter the following medical information: ")
print("---")

#Input
sex = str(input("Please input sex(M/F): "))
age = int(input("Please input age: "))
chol = float(input("Please input total Cholesterol number: "))
smok = str(input("Smoker?(Y/N): "))
hdl = float(input("Please input HDL Cholesterol, in mg/dL: "))
bp = float(input("Please input systolic BP: "))
trea = str(input("Treated for systolic BP?(Y/N): "))

#Convert string variables to float
if smok == "Y":
   smok = True
else:
   smok = False

if trea == "Y":
   trea = True
else:
   trea = False



print("---")

valid = True

#Calculations

#calculate base risk based on age

#Make sure inputs are valid- age must be within 20-79 and sex must be "M" or "F"
if sex != "F" and sex != "M":
   print("Error: Couldn't read sex input.")
   valid = False

#calculate risk from age
if age < 20:
   print("Error: Age too low")
   valid = False
elif age < 35:
   if sex == "F":
       p_age = -7
   else:
       p_age = -9
elif age < 40:
   if sex == "F":
       p_age = -3
   else:
       p_age = -4
elif age < 45:
   p_age = 0
elif age < 50:
   p_age = 3
elif age < 55:
   p_age = 6
elif age < 60:
   p_age = 8
elif age < 65:
   if sex == "F":
       p_age = 10
   else:
       p_age = 10
elif age < 70:
   if sex == "F":
       p_age = 12
   else:
       p_age = 11
elif age < 75:
   if sex == "F":
       p_age = 14
   else:
       p_age = 12
elif age < 80:
   if sex == "F":
       p_age = 16
   else:
       p_age = 13
else:
   print("Error: Age is too high.")
   valid = False

print("Points from age: " + str(p_age))

#calculate points from cholesterol
if valid:
   if age < 40:
       if sex == "F":
           if chol < 160:
               p_chol = 0
           elif chol < 200:
               p_chol = 4
           elif chol < 240:
               p_chol = 8
           elif chol < 280:
               p_chol = 11
           else:
               p_chol = 13
       else:
           if chol < 160:
               p_chol = 0
           elif chol < 200:
               p_chol = 4
           elif chol < 240:
               p_chol = 7
           elif chol < 280:
               p_chol = 9
           else:
               p_chol = 11
   elif age < 60:
       if sex == "F":
           if chol < 160:
               p_chol = 0
           elif chol < 200:
               p_chol = 2
           elif chol < 240:
               p_chol = 4
           elif chol < 280:
               p_chol = 5
           else:
               p_chol = 7
       else:
           if chol < 160:
               p_chol = 0
           elif chol < 200:
               p_chol = 2
           elif chol < 240:
               p_chol = 3
           elif chol < 280:
               p_chol = 4
           else:
               p_chol = 5
   elif age < 70:
       if sex == "F":
           if chol < 160:
               p_chol = 0
           elif chol < 200:
               p_chol = 1
           elif chol < 240:
               p_chol = 2
           elif chol < 280:
               p_chol = 3
           else:
               p_chol = 4
       else:
           if chol < 160:
               p_chol = 0
           elif chol < 200:
               p_chol = 1
           elif chol < 240:
               p_chol = 1
           elif chol < 280:
               p_chol = 2
           else:
               p_chol = 3
   elif age < 80:
       if sex == "F":
           if chol < 160:
               p_chol = 0
           elif chol < 200:
               p_chol = 1
           elif chol < 240:
               p_chol = 1
           elif chol < 280:
               p_chol = 2
           else:
               p_chol = 2
       else:
           if chol < 160:
               p_chol = 0
           elif chol < 200:
               p_chol = 0
           elif chol < 240:
               p_chol = 0
           elif chol < 280:
               p_chol = 1
           else:
               p_chol = 1
if valid:
   print("Points from total cholesterol: " + str(p_chol))


#calculate points from smoking
if valid:
   if smok:
       if sex == "F":
           if age < 40:
               p_smok = 9
           elif age < 50:
               p_smok = 7
           elif age < 60:
               p_smok = 4
           elif age < 70:
               p_smok = 2
           elif age < 80:
               p_smok = 1
       else:
           if age < 40:
               p_smok = 8
           elif age < 50:
               p_smok = 5
           elif age < 60:
               p_smok = 3
           elif age < 70:
               p_smok = 1
           elif age < 80:
               p_smok = 1
   else:
       p_smok = 0

if valid:
   print("Points from smoking: " + str(p_smok))

if valid:
   if hdl < 40:
       p_hdl = 2
   elif hdl < 50:
       p_hdl = 1
   elif hdl < 60:
       p_hdl = 0
   else:
       p_hdl = -1

if valid:
   print("Points from HDL: " + str(p_hdl))

if valid:
   if trea:
       if sex == "F":
           #treated female
           if bp < 120:
               p_bp = 0
           elif bp < 130:
               p_bp = 3
           elif bp < 140:
               p_bp = 4
           elif bp < 160:
               p_bp = 5
           else:
               p_bp = 6
       else:
           #treated male
           if bp < 120:
               p_bp = 0
           elif bp < 130:
               p_bp = 1
           elif bp < 140:
               p_bp = 2
           elif bp < 160:
               p_bp = 2
           else:
               p_bp = 3
   else:
       if sex == "F":
           # untreated female
           if bp < 120:
               p_bp = 0
           elif bp < 130:
               p_bp = 1
           elif bp < 140:
               p_bp = 2
           elif bp < 160:
               p_bp = 3
           else:
               p_bp = 4
       else:
           #untreated male
           if bp < 120:
               p_bp = 0
           elif bp < 130:
               p_bp = 0
           elif bp < 140:
               p_bp = 1
           elif bp < 160:
               p_bp = 1
           else:
               p_bp = 2

if valid:
   print("Points from systolic blood pressure: " + str(p_bp))


if valid:
   p_tot = p_age + p_chol + p_smok + p_hdl + p_bp
   print("Total points: " + str(p_tot))

#find decade risk from points
if valid:
   if sex == "F":
       if p_tot < 9:
           risk = "<1"
       elif p_tot < 13:
           risk = 1
       elif p_tot < 15:
           risk = 2
       elif p_tot == 16:
           risk = 4
       elif p_tot == 17:
           risk = 5
       elif p_tot == 18:
           risk = 6
       elif p_tot == 19:
           risk = 8
       elif p_tot == 20:
           risk = 11
       elif p_tot == 21:
           risk = 14
       elif p_tot == 22:
           risk = 17
       elif p_tot == 23:
           risk = 22
       elif p_tot == 24:
           risk = 27
       else:
           risk = "≥30"
   else:
       if p_tot < 0:
           risk = "<1"
       elif p_tot == 0:
           risk = 1
       elif p_tot == 1:
           risk = 1
       elif p_tot == 2:
           risk = 1
       elif p_tot == 3:
           risk = 1
       elif p_tot == 4:
           risk = 1
       elif p_tot == 5:
           risk = 2
       elif p_tot == 6:
           risk = 2
       elif p_tot == 7:
           risk = 3
       elif p_tot == 8:
           risk = 4
       elif p_tot == 9:
           risk = 5
       elif p_tot == 10:
           risk = 6
       elif p_tot == 11:
           risk = 8
       elif p_tot == 12:
           risk = 10
       elif p_tot == 13:
           risk = 12
       elif p_tot == 14:
           risk = 16
       elif p_tot == 15:
           risk = 20
       elif p_tot == 16:
           risk = 25
       else:
           risk = "≥30"

if valid:
   print("10-year risk is " + str(risk) + "%")