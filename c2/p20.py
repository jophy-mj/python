n=int(input("Enter the limit:"))
l1=[]
l2=[]
for i in range(0,n+1):
  num=int(input("Enter the no:"))
  l1.append(num)
print("Entered list:",l1)
for i in l1:
  if (i%2)!=0:
    l2.append(i)
print("list without even numbers:",l2)
