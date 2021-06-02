name = 'Nidhi'  # outside function

def who():
    print('who am i ?')
    print(f'i am {name}')  # can be access inside fun 

who()


def what():
    print('what r u')
    name = 'god queen'
    print(f'i am {name}')

what()

def update_name():
    global name
    print('old name',name)
    name = 'nidhi chaubey'
    print('new name',name)

who()
print('global variable =>',name)
what()
print('global variable =>',name)
update_name()
print('global variable ==>',name)