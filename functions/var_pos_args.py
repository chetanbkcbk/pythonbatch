def collect(a,b,c,d,*e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
#packing can be seen in function declaration using *args
collect("sonia",10,20,30,40,50,"maria","jalli")

print("-----------")

def distribute(a,b,c,*d):
    print(a)
    print(b)
    print(c)
    print(d)
#UNPACKING can be seen,if i use *iterable in the function call 
l=["sonia",10,20,30,40,50]
distribute(*l)#unpack into pos ar and shud match no of para


def display_student(name,age,degree):
    print(name,"age is",age,degree)

l=['monish',25,'BE']

display_student(*l)




