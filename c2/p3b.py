n=int(input("enter the limit:"))
l=[]
for i in range(0,n):
  num=int(input("enter no:"))
  l.append(num)
print("Entered list:",l)
l1=[i*i for i in l]
print("List of squres:",l1) 

