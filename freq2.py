a="this is an apple,this is great"
b=a.replace(","," ").split()

for i in range(len(b)):
    count=0
    for j in range(len(b)):
        if b[i]==b[j]:
            count=count+1
    duplicat=False

    for k in range(i):
        if b[i]==b[k]:
            duplicat=True
            break

    if not duplicat:
         print(b[i],"-",count)
