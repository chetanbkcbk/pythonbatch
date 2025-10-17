  
fd={99:10,2:20,3:30,4:40}
print(fd)
print(fd[99])#accessing a value using key

fd[99]=100#Updation/modification
print(fd)

#adding an item into dict
fd[5]=55
print(fd)

#setdefault
fd.setdefault(6)
print(fd)

print("-----------")
#get(key) ->returns the value for the key

v=fd.get(199)
print(v)

r=fd.pop(99)
print(r)
print(fd)


i=fd.popitem()
print(i)
print(fd)

k=fd.keys()
print(k)


v=fd.values()
print(v)

it=fd.items()
print(it)

d1={1:100,2:200}
d2={3:300,4:400}
rd=d1.update(d2)
print(rd)



