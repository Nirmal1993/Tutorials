list1 = [1,2,3,5,6]
list2 = [3,2,1,2,3]
#res = list(filter(x in list1, y in list2, x%y ==0,list1,list2))
#res1 = [pow(x,y) for x in list1 for y in list2]
#newlist = []
#for index in range(len(list1)):
#    newlist.append(list1[index]**list2[index])
#print (newlist)

res = list(map(lambda x,y:x**y, list1, list2))
print(res)

