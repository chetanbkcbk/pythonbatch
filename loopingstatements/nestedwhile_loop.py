

'''
i=1
while i<6:
    j=1
    while j<6:
        print(f"{i}*{j}={i*j}")
        j+=1
    i+=1
'''

'''    
i=1
while i<6:
    j=1
    while j<6:
        if j==2 or j==4:
            j+=1
            continue       #continue inside innerwhile loop
        print(f"{i}*{j}={i*j}")
        j+=1
    print("outside")
    i+=1

'''

'''
i=1
while i<6:
    j=1
    while j<6:
        if j==2 or j==4:
            j+=1
            break          #break insid einnerwhile lloop
        print(f"{i}*{j}={i*j}")
        j+=1
    print("outside")
    i+=1
'''
