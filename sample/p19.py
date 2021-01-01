n=int(input("enter a no:"))
e=int(input("enter exponent:"))
p=1
for i in range(1,e+1):
    p=p*n
print("power of",n,"^",e,"is",p)
