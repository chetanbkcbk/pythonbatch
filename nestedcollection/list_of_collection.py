l=[[1,2],(3,4),{5,6},{10:100,20:200},"hello"]#we can
print(l)

print("-----")
t=([1,2],(3,4),{5,6},{10:100,20:200},"hello")
print(t)

print("-----")
st={(3,4),"hello"}#inside set Immutable collection(hashable)
print(st)


##print("-----")
##d={1:[10,20],2:(30,40),3:{50,60},4:{'a':'apple'},5:"orange"}
##print(d)


dk={(30,40):2,"50":5}
print(dk)

fs=frozenset({1,2,4})
print(type(fs))

s={1,22,fs}#frozenset placed inside a set
print(s)

dit={fs:100}#frozenset used as key  inside a dictionary
print(dit)



