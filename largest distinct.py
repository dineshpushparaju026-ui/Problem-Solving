a = [10, 5, 20, 8, 15, 3, 20]
largest=a[0]
secondlargest=a[0]
distinct=[]
for i in range(len(a)):
    if a[i]not in distinct:
     distinct.append(a[i])
print("distinct", distinct)

largest=distinct[0]
secondlargest=distinct[0]
for j in range(len(distinct)):
            if distinct[j]>largest:
                largest=distinct[j]
                

for k in range(len(distinct)):
            if distinct[k]>secondlargest and distinct[k]!=largest:
                secondlargest=distinct[k]

print("largest",largest)
print("secondlargest",secondlargest )

