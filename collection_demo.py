import pandas as pd
p=pd.Series([1,23,34])
print(p)
print("--------")
empty_list=[] #1st empty list
print(empty_list)
print(type(empty_list))
l=len(empty_list)
print(l)

print("--------")

empty_list2=list() #2nd empty list,classname
print(empty_list2)
print(type(empty_list2))
l=len(empty_list2)
print(l)

print("+++++++++")
fl=[10,20,30,40,50,60,70] #filled list creation
print(len(fl))
print(fl[0])#first ele in list
print( fl[len(fl)-1]  )#last ele in list


print(  fl[-1]  )#last ele in list neg index
print(  fl[-len(fl)]  )

fl[5]=600
print(fl)
