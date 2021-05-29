emp ={
    'name':'nidhi chaubey',
    'destignation':'engineer',
    'salary':{
        'basic':120000,
        'da':10000,
        'hra':4000,
        'misc':2000,
    },
    'dept':'account',
    'doj':{
        'year':2000,
        'month':3,
        'day':21
    },
}
print(emp)
print(emp['name'])
print(emp['salary'])


stockprices = dict(google = 234, facebook = 211.23, instagram = 245)
print('another dictionary')
print(stockprices)

# add a value
print('added a value')
stockprices['disney'] = 250.0
print(stockprices)

emp['phone'] = '88626296263'
print(emp)

# update a value
print('updating a value')
stockprices['facebook'] = 180.33
print(stockprices)


emp['dept'] = 'sales'
print(emp)