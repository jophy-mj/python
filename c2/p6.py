l=['jophy','anu','maria','betty']
l2=[]
l3=[]
count=0
for i in l:
    l2=list(i)
    for i in l2:
        l3.append(i)
for i in l3:
    if i=='a':
        count+=1
print("no: of times 'a' occured is:",count)
