a=int(input())
b=int(input())

temp=a
a=b
b=temp
print(a)
print(b)

a = [10, 20, 30, 40, 50]

i = 1
j = 3

a[i] = a[i] + a[j]
a[j] = a[i] - a[j]
a[i] = a[i] - a[j]

print(a)




                           