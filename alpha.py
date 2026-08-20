a=input()

count=0
count1=0
count2=0
count3=0
count4=0

for i in a:
    if i in "aeiou":
        count=count+1

    elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        count1=count1+1

    elif " " in i:
        count2=count2+1

    elif i in "0123456789":
        count3=count3+1

    elif i in "!,#,$":
        count4=count4+1
        

print("vowels",count)
print("consonents",count1)
print("space",count2)
print("digit",count3)
print("special character",count4)
        