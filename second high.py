a=[2,4,56,7,98,1]

largest=+999
second=+999

for i in range(len(a)):
    if a[i]<largest:
        largest=a[i]
print(largest)


for j in range(len(a)):
    if a[j]<second and a[j]!=largest:
        second=a[j]
print(second)
