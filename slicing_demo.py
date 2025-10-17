#slicing

l=[10,20,30,40,50,60,70,80]

print(l[0])#indexing gives u single elem


#slicing gives u a portion from a sequence
# syntax->   ref[startindex:stopindex:stepsize]

#+ve,forward slicing
sl=l[3:len(l):4]
print(sl)

#

##nsl=l[-7:len(l):3]
##print(nsl)

rl=l[-1:-len(l)-1:-1]
print(rl)
'''
s='python in snake'

r=s[::-1]
print(r)

t=(1,2,3,4,5,6,7)

sl_tp=t[1:5:2]
print(type(sl_tp))
'''
