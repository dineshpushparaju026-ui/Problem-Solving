a="programming"
result=""
for j in range(len(a)):
        if a[j] not in a[:j]:
            result=result+a[j]
        else:
            continue
print(result)