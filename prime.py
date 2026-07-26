a=int(input())
count=0
if a<=1:
    print("not prime")

else:
    for i in range(2,a):
      if a%2==0:
        count=count+1
       

      else:
         print("not prime")

    if count==0:
      print("prime")