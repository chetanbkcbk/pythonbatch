def display(**kwargs):
    print(kwargs)
display(name="Chandhan",age=35,salary=60000)

print("-----------")

def display(name,**kwargs):
    print(name)
    print(kwargs)
display(name="Chandhan",age=35,salary=60000)

print("========")
#UNPACKING

def display_student(name,age,degree,**kwargs):
    print(name,age,degree)
    print(kwargs)

d={'name':'Batista',
   'age':25,
   'degree':'BE',
   'exp':10,
   'skill':'django',
   'internship':'microsoft'}


display_student(**d)#unpacking







