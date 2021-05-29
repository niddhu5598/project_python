x = [1,2,1,3,3,4,5,6,6,7,8,9,30]

# NORMAL
x3 = []
for i in x:
    if i%3 == 0:
        x3.append(i)
print(x3)

# filter with lambda
m3 = lambda i: i%3 !=0
output = (list(filter(m3,x)))
print(output)