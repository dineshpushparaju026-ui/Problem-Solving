a="programming"

for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[i]==a[j]:
            count=count+1
           
    if count>1:
     print(a[i],count)
     break
        