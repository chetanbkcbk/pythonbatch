name=input('enter name')
age=input('enter age')
weit=input('enter weit')

#1)'f formatting'
format1=f'Name is {name} Age is {age} Weight is {weit}'
print(format1)

#2)using 'format()'
format2='Name is {} Age is {} Weight is {}'.format(name,age,weit)
print(format2)

#3)to use '% formatting' ,we shud have converted already
age=int(age)
weit=float(weit)
format3='Name is %s Age is %d Weight is %f' %(name,age,weit)
print(format3)


print("-----------------------------------------------")
#to use precisedecimal with float in all 3 formatting,we shud have converted already
weit=float(weit)

format1=f' Weight is {weit :.2f}'
print(format1)
format2=' Weight is {:.3f}'.format(weit)
print(format2)
format3=' Weight is %.1f' %(weit)
print(format3)


'''
n1=int(input('enter the 1st no'))
n2=int(input('enter an 2nd no'))

output=f'multiplying first number {n1} with second number {n2} gives product as {n1*n2}'

print(output)
'''

'''
name=input('enter name')
age=int(input('enter age'))
hit=float(input('enter height'))
print('name is %s age is %d hit is %.2f '%(name,age,hit))
'''
