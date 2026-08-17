secret=50
userguess=int(input())
attempt=0
while userguess!=secret:
    attempt=attempt+1
    if userguess>secret:
        print("high")
        userguess=int(input())

    elif userguess<secret:
        print("low")
        userguess=int(input())

if userguess==secret:
        print("correct")

print("attempts:",attempt)
