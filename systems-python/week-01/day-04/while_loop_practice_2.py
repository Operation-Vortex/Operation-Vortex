
user_command  = ""

while user_command.lower != "quit":
    print("Choose\n Start - Start the the car\n Stop to stop the car\n Quit to quit the game")
    user_command = input("Choose: ")
        
    if user_command.lower == "start":
        print("Car started....going")
        break
        
    elif user_command.lower == "stop":
        print("Car stopped")
        break

    else:
        print("I do not understand that....Try again")
        break