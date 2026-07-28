s="abcdef"
for i in range(len(s)-1):
    if ord(s[i+1])-ord(s[i])==1:
        print(s[i],s[i+1])
    

print(":space")


print(ord("a"))
print(ord("z"))    
print(chr(112))
print(chr(119))
print(chr(ord("a")+1))