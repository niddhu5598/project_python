#operator
#mathematical
a =10
b =4

c= a+b
print("add output",c)

#comparison
x = 32
name = 'nid'

out = x < 23
print('x < 23',out)

out = x > 23
print('x > 23',out)

out = x == 23
print('x == 23',out)

out = x <= 23
print('x <= 23',out)

out = x != 23
print('x != 23',out)

out = name == 'nid'
print("name == 'nid'",out)


#logical

a = 11
b = 4
c = 7

out =a > b and b < 11
print('a > b and b < 11',out)

out =a > b or b > c
print('a > b or b > c',out)

out =a > b or b < 11
print('a > b and b < 11',out)

out = name == 'motu' or name == 'moti'
print(" name == 'motu' or name == 'moti'",out)

out = not len(name) >= 6
print("not len(name) >= 6",out)


#membership
fruits = ['apple', 'banana', 'cherry']
out = 'grapes' in fruits
print("'grapes' in fruits", out)


out = 'apple' in fruits
print("'apple' in fruits", out)


a = 12
# a = a + 10
a += 10 #add 10 to value of a
print("a += 10",a)

a -= 5 #substract 5 from a
print("a -= 5",a)

a *= 3 #mul 3 with a
print("a *= 3",a)

a /= 4 # div 4 with a
print("a /= 4",a)

# integer (int)
a = 5
b = 3456
c = +456
d = -98755

print(type(a),type(b),type(c),type(d))


# float 
a = 5.44
b = 3456.65
c = +0.4569876556789
d = -1.2e-76

print(type(a),type(b),type(c),type(d))

# bool
a = True
b = False



# data structure

# list
a = [1,2,3,4,5,5,6,7]
print(type(a))

# tuple
a = (1,2,3,4,5,5,6,7)
b = 7,3,4,6,4
print(type(a),type(b))

# set
a = {1,2,3,4,5,5,6,7}
b = {7,3,4,6}
print(type(a),type(b))

# dictionary
a = {"name":'apple'}
b = {1:100,2:2987}
print(type(a),type(b))









