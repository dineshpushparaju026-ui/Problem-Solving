a="this is an apple,this is great"
b=a.replace(","," ").split()
dict={}
result=""

for i in b:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1

for i in range(len(b)):
    if b[i] not in b[:i]:
        result=result+b[i]+" "+str(dict[b[i]])+"\n"
    
print(result)
