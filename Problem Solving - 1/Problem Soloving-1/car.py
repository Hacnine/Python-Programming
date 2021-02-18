strings = input('If you want help type "Help": ').lower()
if strings == 'help':
    instruction = '''start - to start the car
    stop - to stop the car
    end - to end the help service 
    exit - to exit out of this service'''
    print(instruction)

get_inc = ""
started = False

while True:
    get_inc = input(">").lower()
    if get_inc == "start":
        if started:
            print("Already started...")
        else:
            started = True
            print("started...")
    elif get_inc == "stop":
        if not started:
            print("Already stop...")
            print(started)
        else:
            started = False
            print("stop!...")
    elif get_inc == "end":
        print("ended.")
    elif get_inc == "exit":
        break
    else:
        print("I don't understand that.")
