n=input("enter a word:")
l=list(n)
l2=[]
for i in l:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        l2.append(i)
print("List of vowels in",n,"is",l2)
    
    
