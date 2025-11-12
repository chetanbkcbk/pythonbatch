for num in range(1,3):
    for val in range(1,11):
        print(f"{num} *{val}={num*val}")
    
print("-------")

for num in range(2,0,-1):
    for val in range(10,0,-1):
        print(num,"X",val,"=",num*val)
print("========")

l1=['dosa','idli']
l2=['c hutney','sambhar']

for dish in l1:
    for side in l2:
        print(dish,"->",side)
