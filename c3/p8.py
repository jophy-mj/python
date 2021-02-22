def longest(a):
    max1=len(a[0])
    temp=a[0]
    for i in a:
        if (len(i)>max1):
            max1=len(i)
            temp=i
    print("The word with longest length = ",temp,"and length = ",max1)
a=["one","two","three"]
longest(a)
