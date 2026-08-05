s='aaabbbcdd'
count=1

for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count=count+1
    else:
        print(s[i],count,sep="",end="")
        count=1
print(s[i],count,sep="")