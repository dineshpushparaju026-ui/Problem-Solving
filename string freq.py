a="iateapple"

for i in range(len(a)):
    if a[i] not in a[:i]:
    
       count=0
       for j in range(len(a)):
            if a[i]==a[j]:
              count=count+1
       print(a[i],count)