import random
list1 = []
i = 5
y=[2,6,2,9,2]
while(i>0):
    i-=1
    list1.append(random.randint(0,9))
print (list1)
sq=list(map(lambda x,y: x**y,list1,y))
print(sq)
res =list(filter(lambda x:x%2==0, sq))
print(res)


