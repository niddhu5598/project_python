xset = {1,2,3,4,5,6,7}
xtup = (1,2,3,41,2,3,1,2,1,2,3,1,5)
xdict = {'a': 'apple','b': 'banana'}


print('set')
for i in xset:
    print(i,end=' ,')


print('\ntuple')
for i in xtup:
    print(i,end=',')



print('\ndictionary')
for i in xdict:
    print(i,end='||')