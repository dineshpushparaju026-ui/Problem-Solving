
s="abdef"
for i in range(len(s)-1):
    if ord(s[i+1])-ord(s[i])>1:
        print(chr(ord(s[i])+1))
