#1
'''i=2 infinite loop
while i!=21:
    if i<21:#remainder when divided by2 equal to 0
        print(i)
    i=i+2
'''
print("-----")
#2

for i in range(1,11):
    if i ==5:
        continue
    print(i)

#3
n=1
while n<11:
    print(6,"*",n,"=",6*n)
    n=n+1

#4
l=[80,56,20,50,40,45]
for ele in l:
    if ele>40 and ele<55:
        print(ele)
        break
#5
students={"Ravi":85,"Sara":90,"kiran":75}

itms=students.items()

for k,v in itms:
    print(k,v)

#6

def to_powerof(a,b):
    return a**b
print(to_powerof(10,2))

#7
s1={1,2,3}
fs=frozenset(s1)
s2={4,5,fs}
print(s2)

#8
def accept_marks(*marks):
    for mark in marks:
        if mark>75:
            print(mark)


accept_marks(45,55,35,76,83,2,2,5,74,97,856,86)

#9
def register_user(**details):
    print(details)
register_user(name='dharun',age=45,gender='male')


#10
data=[[1,2,3],[4,5,6],[7,8,9]]
for il in data:
    for ele in il:
        print(ele,end=' ')
    print()

#11
s=-20
while s<3:
    if s%2==1:
        print(s)
    s=s+1
    
