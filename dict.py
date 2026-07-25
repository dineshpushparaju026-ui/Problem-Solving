user={"name":"alice","age":27,"role":"developer"}
print(user["name"])
print(user.get("bonus"))


user["age"]=26
user["city"]="trichy"

del user["role"]
print(user.get("city"))

print(user)
