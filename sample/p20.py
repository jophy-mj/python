n=int(input("enter no:"))
rev=0
temp=n
while(temp>0):
    r=temp%10
    rev=(rev*10)+r
    temp=temp//10
print("reverse of",n,"is",rev)
if(n==rev):
    print(n,"is palindrome")
else:
    print(n,"is not palindrome")
    
