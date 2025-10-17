#1)append(object) adds an element to the end of the list
#2)insert(index,object)  adds an element to specific index,existing ele shifts 1 positon to right
#3)count(object)-> returns the no of occurances of an element
#4)index(object)-> returns the index of FIRST Occurance of that element
#4.1)index(object,start)->
#4.2)index(object,start,end)->

el=[]

fl=[10,20,30,2,41,82,10,10,20]
print(fl)

print(fl.index(10))
print(fl.index(20,1,4))


#5)pop()->

ele=fl.pop()
print(ele)

print(fl)

#5.1)pop(index)->

rem=fl.pop(-3)
print(rem)
print(fl)

e=fl.remove(10)#6)removes the first occurance of the value
print(e)
print(fl)

fl.reverse()
print(fl)

fl.sort()
print(fl)

fl.clear()#7) removes all element from the list
print(fl)




l2=[98,87,76,65]

l2.extend([11,22,33,44])#8) adds the leemtn of 1 list inside another list
print(l2)

