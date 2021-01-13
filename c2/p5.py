n=int(input("Enter limit:"))
l=[]
l2=[]
for i in range(0,n+1):
    no=int(input("enter no:"))
    l.append(no)
for i in l:
    if i<100:
        l2.append(i)
    else:
        l2.append('over')
print(l2)
