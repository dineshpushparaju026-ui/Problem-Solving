a = [3, 8, 5, 10, 12, 7, 6]
count=0
count1=0
for i in a:
    if i%2==0:
       count=count+1
     
    else:
       count1=count1+1

print("even",count)
print("odd",count1)