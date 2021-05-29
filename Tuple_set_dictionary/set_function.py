a = {1,2,3,4,5,6,7,8,9}
b = {2,3,4,5,6}
c = {7,8,9}
d = {11,113,145,56}
e = {33,3,44,45,6,7,8}
print(a.issuperset(c),'a is superset of c')
print(a.issuperset(d),'a is superset of d')

if b.issubset(a):
    print("b is subset of a")

else:
    print('b is not subset of a')
if e.issubset(d):
    print('e is subset of d')
else:
    print('e is not a subset of d')

if a.isdisjoint(e):
    print('a and e me koi rishta hai')
else:
    print('a and e are connected')
if b.isdisjoint(d):
    print('b and d me koi rishta ni hai')
else:
    print('b and d are connected')
# union
print('union')
print(a.union(d))
print(a|d)

# intersection
print('intersection')
print(a.intersection(d))
print(a&d)

# difference
print('difference')
print(a.difference(d))
print(a-d)

# symmetric
print('symmetric')
print(a.symmetric_difference(d))
print(a^d)