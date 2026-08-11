a="abcdf"
alphabet="abcedgfhijkl"

for i in alphabet:
    if i in a:
       continue

    else:
        print(i)
        break

for ch in alphabet:
    if ch not in a:
        print("missing character",ch)
        break