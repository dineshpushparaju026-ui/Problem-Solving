a=[1,2,3,6,8,11]
target=14
flag=False
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==target:
         flag=True
         print(a[i],a[j])
         break

    if flag:
      break