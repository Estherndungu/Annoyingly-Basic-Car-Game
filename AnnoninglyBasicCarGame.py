print("type 'help' to see game commands")
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("Car is already started")
        else:
            started = True
            print("car has started... ")
    elif command == 'stop':
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("car has stopped....")
    elif command == 'help':
        print("""
Start - to start the car
stop - to stop the car
quit - to terminate the game""")
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that")