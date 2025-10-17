es=set()
print(type(es))

fs={10,4.7,10,10,10,False,99-0.0j}
print(fs)

fs.add(1)#adds an element randomly into a set
print(fs)

##a=es.pop()#removes and reurns arbitrary ele from set
##print(a)
##print(fs)

##fs.remove(470)
##print(fs)

fs.discard(470)
print(fs)


fs.clear()
print(fs)

s1={10,20,30}
s2={10}
print("----------------")

print(s2)

us=s1.union(s2)#returns a new set contaning unique element from both sets
print(us)
ins=s2.intersection(s1)
##returns a new set contaning common elements from both sets
print(ins)

#returns False if There are common elemnts btw both sets
b=s1.isdisjoint(s2)
print(b)

d=s2.difference(s1)
print(d)

#returns a new set containing all uncommon ele of both
ue=s1.symmetric_difference(s2)
print(ue)

s1.intersection_update(s2)
print(s1)


