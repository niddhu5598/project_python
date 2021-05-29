for i in range(1,101,10):
    print(i,'\t',i**2)

for i in range(1,102,10):
    print(str(i).ljust(5),str(i**2).ljust(10),str(i**3).ljust(10),str(i**4).ljust(10))

for i in range(1,102,10):
    print(str(i).ljust(5),str(i**2).rjust(10),str(i**3).rjust(10),str(i**4).rjust(10))



for i in range(1,15,2):
    print(i* '$')

for i in range(1,15,2):
    print((i* '#').rjust(15))

for i in range(1,15,2):
    print((i* '&').center(15))


