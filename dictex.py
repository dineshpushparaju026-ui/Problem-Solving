def store(shop,my_product):    
    total=0
    for item in my_product:
        if item in shop:
            total=total+shop[item]
    return total

shop = {"apple": 1.5, "banana": 0.75, "milk": 2.50}        
my_product = ["apple", "milk", "water", "apple"]  

print(store(shop,my_product))