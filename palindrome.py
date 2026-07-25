a=input()


reversed=""

for re in a:
    reversed=re+reversed

if a==reversed:
    print("palindrome is found")

else:
    print("palindrome is not found")