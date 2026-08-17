secret=50
userguess=int(input())
attempt=1
while userguess!=secret and attempt<5:
    if userguess>secret:
        print("high")
        userguess=int(input())

    elif userguess<secret:
        print("low")
        userguess=int(input())
    attempt=attempt+1
         

if userguess==secret:
        print("correct")

if attempt==5 and userguess!=secret:
    print("game over")
