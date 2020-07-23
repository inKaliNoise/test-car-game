# car game

choose = input(">")

# help list
if choose.lower() == 'help':
    print('''
    start - to start the car
    stop - to stop the car
    quit - to exit''')
    choose = input(">")

# game engine 
while choose.lower() != 'quit':
    if choose.lower() == 'start':
        print('Car started...Ready to go!')
        choose = input(">")
    elif choose.lower() == 'stop':
        print('Car stopped.')
        choose = input(">")
    else:
        print("I don't understand that...")
        choose = input(">")