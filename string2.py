name="iateapple"
dict={}
result=""
for ch in name:
    if ch in dict:
        dict[ch]=dict[ch]+1

    else:
       dict[ch]=1
    
for i in range(len(name)):
    if name[i] not in name[:i]:
        result=result+name[i]+str(dict[name[i]])
    
print(result)