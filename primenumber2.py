a=list(range(1,100))


for i in range(len(a)):
 count=0
 if a[i]<1:
    print("not prime")
    count=0

 else:
    for j in range(1,a[i]+1):
        if a[i]%j==0:
            count=count+1
   

    if count==2:
      print(a[i])
    



 