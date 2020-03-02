# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         Esther Li       828007859
#               Dacheng Jiang   428007586
#               Rong Xu         928009312
#
# Section:		ENGR 102 554
# Assignment:	Lab 05 A
# Date:		    24 September 2019

gender=str(input("please input your gender('M' means man/'W' means woman)"))
age=int(input("please input your age"))
chol=float(input("please input your total Cholesterol"))
smo=str(input("please input the info if you are a smoker('Y' means yes/'N' means no)"))
hdl=float(input("please input your HDL"))
syst=str(input("please input if you are treated with systolic BP('Y' means yes/'N' means no)"))
syst_bp=float(input("please input your systolic BP"))

tot_p_m=0
tot_p_w=0
age_p_m=0
chol_p_m=0
hdl_p=0
syst_p_m=0
smo_p_m=0
hdl_p=0
smo_p_w=0
syst_p_w=0
chol_p_w=0
age_p_w=0

if gender == 'M':
    #global age_p_m
    if age<=34 and age>=20:
        age_p_m = -9 
    elif age<=39 and age>=35:
        age_p_m = -4 
    elif age<=44 and age>=40:
        age_p_m = 0
    elif age<=49 and age>=45:
        age_p_m = 3
    elif age<=54 and age>=50:
        age_p_m = 6
    elif age<=59 and age>=55:
        age_p_m = 8
    elif age<=64 and age>=60:
        age_p_m = 10 
    elif age<=69 and age>=65:
        age_p_m = 11 
    elif age<=74 and age>=70:
        age_p_m = 12 
    elif age<=79 and age>=75:
        age_p_m = 13 
    if age<=39 and age>=20:
        #global chol_p_m
        #global smo_p_m
        if chol<160:
            chol_p_m = 0 
        elif chol>=160 and chol<=199:
            chol_p_m = 4 
        elif chol>=200 and chol<=239:
            chol_p_m = 7 
        elif chol>=240 and chol<=279:
            chol_p_m = 9 
        elif chol>=280:
            chol_p_m = 11 
        if smo=='N':
            smo_p_m=0
        elif smo=='Y':
            smo_p_m=8
    if age<=40 and age>=49:
        if chol<160:
            chol_p_m=0 
        elif chol>=160 and chol<=199:
            chol_p_m=3 
        elif chol>=200 and chol<=239:
            chol_p_m=5 
        elif chol>=240 and chol<=279:
            chol_p_m=6 
        elif chol>=280:
            chol_p_m=8 
        if smo=='N':
            smo_p_m=0
        elif smo=='Y':
            smo_p_m=5
    if age<=50 and age>=59:
        if chol<160:
            chol_p_m=0 
        elif chol>=160 and chol<=199:
            chol_p_m=2 
        elif chol>=200 and chol<=239:
            chol_p_m=3 
        elif chol>=240 and chol<=279:
            chol_p_m=4 
        elif chol>=280:
            chol_p_m=5 
        if smo=='N':
            smo_p_m=0
        elif smo=='Y':
            smo_p_m=3
    if age<=60 and age>=69:
        if chol<160:
            chol_p_m=0 
        elif chol>=160 and chol<=199:
            chol_p_m=1 
        elif chol>=200 and chol<=239:
            chol_p_m=1 
        elif chol>=240 and chol<=279:
            chol_p_m=2 
        elif chol>=280:
            chol_p_m=3 
        if smo=='N':
            smo_p_m=0
        elif smo=='Y':
            smo_p_m=1
    if age<=70 and age>=79:
        if chol<160:
            chol_p_m=0 
        elif chol>=160 and chol<=199:
            chol_p_m=0 
        elif chol>=200 and chol<=239:
            chol_p_m=0 
        elif chol>=240 and chol<=279:
            chol_p_m=1 
        elif chol>=280:
            chol_p_m=1 
        if smo=='N':
            smo_p_m=0
        elif smo=='Y':
            smo_p_m=1
    if hdl>=60:
        hdl_p=-1
    elif hdl>=50 and hdl<=59:
        hdl_p=0
    elif hdl>=40 and hdl<=49:
        hdl_p=1
    elif hdl<40:
        hdl_p=2
    if syst=='Y':
        if syst_bp<120:
            syst_p_m=0
        elif syst_bp<=129 and syst_bp>=120:
            syst_p_m=1
        elif syst_bp<=139 and syst_bp>=130:
            syst_p_m=2
        elif syst_bp<=159 and syst_bp>=140:
            syst_p_m=2
        elif syst_bp>=160:
            syst_p_m=3
    if syst=='N':
        if syst_bp<120:
            syst_p_m=0
        elif syst_bp<=129 and syst_bp>=120:
            syst_p_m=0
        elif syst_bp<=139 and syst_bp>=130:
            syst_p_m=1
        elif syst_bp<=159 and syst_bp>=140:
            syst_p_m=1
        elif syst_bp>=160:
            syst_p_m=2
elif gender=='W':
    if age<=34 and age>=20:
        age_p_w=-7
    elif age<=39 and age>=35:
        age_p_w=-3
    elif age<=44 and age>=40:
        age_p_w=0
    elif age<=49 and age>=45:
        age_p_w=3
    elif age<=54 and age>=50:
        age_p_w=6
    elif age<=59 and age>=55:
        age_p_w=8
    elif age<=64 and age>=60:
        age_p_w=10
    elif age<=69 and age>=65:
        age_p_w=12
    elif age<=74 and age>=70:
        age_p_w=14
    elif age<=79 and age>=75:
        age_p_w=16
    if age<=39 and age>=20:
        if chol<160:
            chol_p_w=0
        elif chol>=160 and chol<=199:
            chol_p_w=4
        elif chol>=200 and chol<=239:
            chol_p_w=8
        elif chol>=240 and chol<=279:
            chol_p_w=11
        elif chol>=280:
            chol_p_w=13
        if smo=='N':
            smo_p_w=0
        elif smo=='Y':
            smo_p_w=9
    if age<=40 and age>=49:
        if chol<160:
            chol_p_w=0
        elif chol>=160 and chol<=199:
            chol_p_w=3
        elif chol>=200 and chol<=239:
            chol_p_w=6
        elif chol>=240 and chol<=279:
            chol_p_w=8
        elif chol>=280:
            chol_p_w=10
        if smo=='N':
            smo_p_w=0
        elif smo=='Y':
            smo_p_w=7
    if age<=50 and age>=59:
        if chol<160:
            chol_p_w=0
        elif chol>=160 and chol<=199:
            chol_p_w=2
        elif chol>=200 and chol<=239:
            chol_p_w=4
        elif chol>=240 and chol<=279:
            chol_p_w=5
        elif chol>=280:
            chol_p_w=7
        if smo=='N':
            smo_p_w=0
        elif smo=='Y':
            smo_p_w=4
    if age<=60 and age>=69:
        if chol<160:
            chol_p_w=0
        elif chol>=160 and chol<=199:
            chol_p_w=1
        elif chol>=200 and chol<=239:
            chol_p_w=2
        elif chol>=240 and chol<=279:
            chol_p_w=3
        elif chol>=280:
            chol_p_w=4
        if smo=='N':
            smo_p_w=0
        elif smo=='Y':
            smo_p_w=2
    if age<=70 and age>=79:
        if chol<160:
            chol_p_w=0
        elif chol>=160 and chol<=199:
            chol_p_w=1
        elif chol>=200 and chol<=239:
            chol_p_w=1
        elif chol>=240 and chol<=279:
            chol_p_w=2
        elif chol>=280:
            chol_p_w=2
        if smo=='N':
            smo_p_w=0
        elif smo=='Y':
            smo_p_w=1
    if hdl>=60:
        hdl_p=-1
    elif hdl>=50 and hdl<=59:
        hdl_p=0
    elif hdl>=40 and hdl<=49:
        hdl_p=1
    elif hdl<40:
        hdl_p=2
    if syst=='Y':
        if syst_bp<120:
            syst_p_m=0
        elif syst_bp<=129 and syst_bp>=120:
            syst_p_m=3
        elif syst_bp<=139 and syst_bp>=130:
            syst_p_m=4
        elif syst_bp<=159 and syst_bp>=140:
            syst_p_m=5
        elif syst_bp>=160:
            syst_p_m=6
    if syst=='N':
        if syst_bp<120:
            syst_p_m=0
        elif syst_bp<=129 and syst_bp>=120:
            syst_p_m=1
        elif syst_bp<=139 and syst_bp>=130:
            syst_p_m=2
        elif syst_bp<=159 and syst_bp>=140:
            syst_p_m=3
        elif syst_bp>=160:
            syst_p_m=4
if gender=='M':
    tot_p_m=age_p_m+chol_p_m+syst_p_m+smo_p_m+hdl_p
else:
    tot_p_w=age_p_w+chol_p_w+syst_p_w+smo_p_w+hdl_p
print(age_p_m)
print(chol_p_m)
print(smo_p_m)
print(hdl_p)
print(syst_p_m)
print(tot_p_m)
print(tot_p_w)
res="10-Year risk is"

if tot_p_m<=4 or tot_p_w<=12:
    print(res,"1%")
elif (tot_p_m<=6 and tot_p_m>=5) or (tot_p_w<=14 and tot_p_w>=13):
    print(res,"2%")
elif tot_p_m==7 or tot_p_w==15:
    print(res,"3%")
elif tot_p_m==8 or tot_p_w==16:
    print(res,"4%")
elif tot_p_m==9 or tot_p_w==17:
    print(res,"5%")
elif tot_p_m==10 or tot_p_w==18:
    print(res,"6%")
elif tot_p_m==11 or tot_p_w==19:
    print(res,"8%")
elif tot_p_m>=17 or tot_p_w>=25:
    print(res,"more than 30%")
elif tot_p_m==12:
    print(res,"10%")
elif tot_p_m==13:
    print(res,"12%")
elif tot_p_m==14:
    print(res,"16%")
elif tot_p_m==15:
    print(res,"20%")
elif tot_p_m==16:
    print(res,"25%")
elif tot_p_w==20:
    print(res,"11%")
elif tot_p_w==21:
    print(res,"14%")
elif tot_p_w==22:
    print(res,"17%")
elif tot_p_w==23:
    print(res,"22%")
elif tot_p_w==24:
    print(res,"27%")