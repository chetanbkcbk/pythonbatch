company=[
    {
        'name':'amy',
        'age':21,
        'salary':21000,
        'dept':'IT'
        },

    {
        'name':'ben',
        'age':15,
        'salary':8000,
        'dept':'Sales'
        },
         {'name':'chad','age':51,'salary':88000,'dept':'HR'}
         ]
for ind in company:
    if ind['salary']>10000: 
        print(ind['name'])
