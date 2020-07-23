# car game

choose = ""
speed = 0

# game engine
while True:
    choose = input(">").lower()
    if choose == 'start' and speed < 29:
        print('Car started...Ready to go!')
        speed += 30
    elif choose == 'start' and speed > 29:
        speed += 30
        print(f'the car speed is {speed} km/h')
        if speed > 329:
            speed -= 30
            print("It's maximal speed in this car")
    elif choose == 'stop':
        speed -= 70
        if speed >= 0:
            print(f'the slowed down to {speed} km/h')
        if speed < 0:
            print('Car stopped.')
    elif choose == 'help':
        print('''start - to start the car
stop - to stop the car
quit - to exit''')
    elif choose == 'quit':
        break
    else:
        print("I don't understand that...")