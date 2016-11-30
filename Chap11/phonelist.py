contacts = {}   # The global telephone contact list

running = True

while running:
    command = input('A)dd  D)elete   L)ook up   Q)uit: ')
    if command == 'A' or command == 'a' :
        name = input('Enter new name:')
        print('Enter phone number for', name, end=':')
        number = input()
        contacts[name] = number
    elif command == 'D' or command == 'd':
        name = input('Enter name to delete :')
        del contacts[name]
    elif command == 'L' or command == 'l':
        name = input('Enter name :')
        print(name, contacts[name])
    elif command == 'Q' or command == 'q':
        running = False
    elif command == 'dump':   # Secret command
        print(contacts)
    else:
        print(command, 'is not a valid command')
