#QUE1 PRIME NO.
for i in range(1,51):
    if i==50:
        break
    else:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i,end=' ') 

#que2
a = int(input('entre the list of cricketer:'))
print('enter name of cricketers:')
b = []
for i in range(a):
    name = input()
    if name == name.title():
        b.append(name)
print(b)       

#QUE 
names = ['nidhi','ritik','prateek','aarya','nitika','mohan','rohan']
print(names)

name_containing_a = [name for name in names if 'a' not in name]
name_containing_o = [name for name in names if 'o' not in name]

print(name_containing_a)
print(name_containing_o)
