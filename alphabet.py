a="abcdf"
alphabet="abcedgfhijkl"


for ch in alphabet:
    if ch not in a:
        print("missing character",ch)
        break