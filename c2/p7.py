l1=[2,4,8,1,10]
l2=[2,3,1,9,5,6]
l3=[]
s=0
f=0
n_l1=len(l1)
n_l2=len(l2)
if n_l1==n_l2:
    print("Both lists have same length")
else:
    print("Both lists have different length")
for i in l1:
    s=s+i
for i in l2:
    f=f+i
if f==s:
    print("Both lists sum to same value")
else:
    print("Both lists sum to different value")

