#QUE_1
for x in range(1500,2700):
    if(x%5 == 0) and (x%7 == 0):
        print(x,end=' ')

#QUE_2
even = 0
odd = 0
for i in range(1,50):
    if i%2 == 0:
        even += 1
    else:
        odd += 1
print('all the even',even)
print('all the odd',odd)


#QUE_3
a = 0
b = 1
print(a)
while(b<51):
    c = a
    a = b
    b = c+a
    print(b)

#QUE_4
name = input("enter the name :")

for char in range(len(name) -1,-1,-1):
    print(name[char],end='||')