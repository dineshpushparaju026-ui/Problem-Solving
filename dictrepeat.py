a="aabbcde"
dict={}

for i in a:
    if i in dict:
        dict[i]=dict[i]+1

    else:
        dict[i]=1

print(dict)

for i in a:
    if dict[i]==1:
        print(i)
        break