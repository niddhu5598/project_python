cir = lambda r: 2*r*3.14
data = [2,3,6,4.65,8,2.98]
results =[]

# normal
for radius in data:
    output = cir(radius)
    results.append(output)
print(results)

# comprehension
results = [cir(radius) for radius in data]
print(results)


# map function
results = list(map(cir,data))
print(results)