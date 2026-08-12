a=[10,20,30,40,50]

for  i in range(1,len(a)-1):
    print(a[i])

#largest
a = [10, 5, 20, 8, 15, 3]
largest=a[0]
secondlargest=a[0]
for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]
print(largest)

for j in range(len(a)):
    if a[j]>secondlargest and a[j]!=largest:
        secondlargest=a[j]
print("second largest",secondlargest)
 #smallest
a = [10, 5, 20, 8, 15, 3]
smallest=a[0]
for i in range(len(a)):
    if a[i]<smallest:
      smallest=a[i]
print(smallest)
