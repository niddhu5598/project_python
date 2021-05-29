x = [1,2,3,4,5,6]

x2 = []
for i in x:
    sqr = i**2
    x2.append(i**2)
print(x)
print(x2)


# comprehension
x = [1,2,3,4,5,6,7,8]
X = [i**2 for i in x]
print(X)