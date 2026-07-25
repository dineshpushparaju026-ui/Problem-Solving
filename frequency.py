a=[1,2,3,2,5,3,2,3,45]

for i in range(len(a)):
      
            count=0


            for j in range(len(a)):
             if a[i]==a[j]:
              count=count+1
  
            print(a[i],count)


             

a = [1, 2, 3, 2, 5, 3, 2, 3, 45]

visited=[]
for i in range(len(a)):
    if a[i] in visited:
        continue
    count=0

    for j in range(len(a)):
      if a[i]==a[j]:
         count=count+1
    
    print(a[i],count)

    visited.append(a[i])


