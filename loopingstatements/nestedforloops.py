'''
for i in range(1,6): #nested for
    for j in range(1,6):
        print(f"{i} * {j} ={i*j}")
    print("outside")
'''

'''
for i in range(1,6): #nested for and continue inside outerfor
    for j in range(1,6):
        if i==2:
            break
        print(f"{i} * {j} ={i*j}")
    print("outside")
'''


'''
for i in range(1,6): #nested for and continue inside innerfor
    for j in range(1,6):
        if i==j:
            continue
        print(f"{i} * {j} ={i*j}")
    print("outside")
'''


'''
for i in range(1,6): #nested for and continue inside OUTERFOR
    if i==2 or i==4:
        continue
    for j in range(1,6):
        print(f"{i} * {j} ={i*j}")
    print("outside")
'''


for i in range(1,6): #nested for and break inside OUTERFOR
    if i==2 or i==4:
        break
    for j in range(1,6):
        print(f"{i} * {j} ={i*j}")
    print("outside")

