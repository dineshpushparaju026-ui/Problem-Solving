a="programming"
result=""
for i in range(len(a)):

    for j in range(i):
        if a[i]==a[j]:
            break
  
    else:
            print(a[i],end="")
