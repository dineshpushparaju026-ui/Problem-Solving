def count(text):
    counter={}
    for ch in text:
        counter[ch]=counter.get(ch,0)+1
    return(counter)
print(count("hello"))


