word=input("Enter the sentence:")
count=0
l=word.split(" ")
print(l)
for i in l:
    for j in l:
        if i==j:
            count+=1

            
