def collatz(x):
    lists= [x]
    if x<1 :
        return []
    while x > 1:
        if x% 2==0:
            x=x/2
        else:
            x=x*3+1
        lists.append(x)
    return(lists)
x = int(input("please input a integer:"))
x = collatz(x)
print(x)