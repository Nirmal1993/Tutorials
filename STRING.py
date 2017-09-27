string = input("")
d= {"UPPER":0, "LOWER":0}
for char in string:
    if char.isupper():
        d["UPPER"]+=1 
    elif char.islower():
        d["LOWER"]+=1
    else:
        pass
print("UPPER CASE:",d["UPPER"])
print("LOWER CASE:",d["LOWER"])

