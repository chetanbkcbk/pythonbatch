company={
    "emp1":{
        'name':'amy',
        'age':21,
        'salary':21000,
        'dept':'IT'
        },

    "emp2":{
        'name':'ben',
        'age':15,
        'salary':8000,
        'dept':'Sales'
        },
         "emp3":{'name':'chad','age':51,'salary':88000,'dept':'HR'}
         }
##print(company['emp1'])
##print(company.get('emp1'))

for ok in company:
    print(company[ok].get('name'))
    #print(company[ok]['name'])



