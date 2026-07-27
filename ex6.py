a=[1,2,3,4]

for i in range(len(a)):
   b=a.copy()
   del b[i]

   mul=1

   for j in range(len(b)):

      mul=mul*b[j]
   print(mul)

a=[1,2,3,4]

for i in range(len(a)):
   mul=1

   for j in range(len(a)):

      if i!=j:

         mul=mul*a[j]
   print(mul)