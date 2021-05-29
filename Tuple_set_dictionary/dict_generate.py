contacts = {'help': 100}
print('your temp contact book')
while True:
    name = input("=> enter contact name :")
    if name:
        if name in contacts:
            print('=>contact found')
            print(f'=>{name} : {contacts[name]}')
        else:
             print('==> contact not found')
             update = input('>> do you want to add the contact(Y/N)?')
             if update.lower() == 'y':
                  number = input(f'>>> enter contact number for {name}:')
                  contacts[name] = number
                  print(f'=> contact update for {name}')
    else:
        print('closing contact book')
        break


               