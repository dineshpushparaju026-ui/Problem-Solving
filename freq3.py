a="this is an apple,this is great"
b=a.replace(","," ").split()

for i in range(len(b)):
    if b[i] not in b[:i]:
        count=0
        for j in range(len(b)):
           if b[i]==b[j]:
            count=count+1
        print(b[i],count)


    
