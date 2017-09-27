values =input()
numbers = [x for x in values.split(",")if int(x)%2!=0]
print(",".join(numbers))
numb=list(filter(lambda x:int(x)%3==0,numbers))
print(numb)

