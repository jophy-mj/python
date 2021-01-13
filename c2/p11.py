a=int(input("Enter 1st no:"))
b=int(input("Enter 2st no:"))
c=int(input("Enter 3st no:"))
if((a>b)and(a>c)):
    print("Largest no is ",a)
elif((b>a)and(b>c)):
    print("Largest no is ",b)
else:
    print("Largest no is ",c)
