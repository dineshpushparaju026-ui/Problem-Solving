a = [1,6,7,4,9,12]
b=[1,11,13,8]

c=[]

n=min(len(a),len(b))
for i in range(n):
    c.append(a[-(i+1)])
    c.append(b[-(i+1)])
c.extend(a[:(-n)])
c.extend(b[:(-n)])

print(c)