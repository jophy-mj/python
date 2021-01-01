def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if((greater%x==0) and (greater%y==0)):
            lcm=greater
            break
        greater += 1
    return lcm
a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
print("LCM=",lcm(a,b))
