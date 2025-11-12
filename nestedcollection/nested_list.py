'''nl=[[10,20,30],[40,50,60],[70,80,90],[100,0,0]]

for innerlist in nl:
    for mark in innerlist:
        print(mark)
    print("--------")
'''

students=[['amy',25,'python'],['ben',34,'java'],['chad',12,'c']]

for innerlist in students:
    for ele in innerlist:
        print(ele)
    print("---")

##for student in students:
##    print(student[0],"is enrolled to",student[-1])

for student in students:
    if 'java' in student:
        print(student[0])
 
