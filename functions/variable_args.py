def mean(*numbers):
    if numbers:
        print("mean=>",sum(numbers)/len(numbers))

mean()
mean(1)
mean(12,3,4,4,5,6,7,8)
mean(12,23,4,5,5,78,88,3,3,34,4,5,5,6,6,7,77,42,32,42)


def agg(*numbers, operation = 'sum'):
    if numbers:
        if operation == 'sum':
            print('total',sum(numbers))
        elif operation == 'mean':
            print('mean',sum(numbers)/len(numbers))
        elif operation == 'max':
            print('max',max(numbers))

agg(12,3,4,5,5,6,78,)
agg(1,2,3,4,5,6,7,8,9,operation = 'mean')
agg(1,1,1,1,1,1,2,2,2,2,3,3,3,6544,4,5,5,5,5,6,6,6,7,7,7,operation='max')
agg(1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,operation='sum')



def settings(**info):
    for k,v in info.items():
        print(k,v)

settings(color= 'red',x=23,y=34,size=(22,34))
settings(font='calibri',fontsize=20,rotation=100,fontcolor='black')