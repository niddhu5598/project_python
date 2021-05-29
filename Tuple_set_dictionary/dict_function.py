fruits = {'apple': 100, 'banana':60,
         'cherry':150, 'dragonfruit':200}
print(fruits) 
print('updating values in dict')

new_fruits = {'guava': 35, 'chiku':50}
fruits.update(new_fruits)
print(fruits)

print('removing value from dict')

fruits.pop('cherry')
print(fruits)

if 'orange' in fruits:
    fruits.pop('orange')
    print(fruits)
else:
    print('orange not found')


last_item_removed = fruits.popitem()
print(fruits)
print(f'{last_item_removed} removed from fruits')

# accessing value from dict
print(fruits['apple'])

# better version to access value from dict
print('using to get method in dict')
print(fruits.get('apple'))
print(fruits.get('Apple'))

print('using get() with default value, in dict')
print(fruits.get('Apple','price not found'))
print(fruits.get('banana','price not found'))

# accessing keys, values and pair wisw item in dict
print(fruits.values())
print(fruits.keys())
print(fruits.items())

print('looping in dict')
print('=> normal loop get only keys')

for i in fruits:
    print(i)

print('==> get only values')
for i in fruits.values():
    print(i)

print('=> get both key and value')
for k,v in fruits.items():
    print(k,'-->',v)