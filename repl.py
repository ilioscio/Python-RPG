def repl(character):
    commands = [
        "look", #returns the current room's description, and lists any items in view, and available paths
        "move", #move on a given path from the current room
        "help", #display help
        "inventory", #lists any items in inventory
        "quit" #quits the game
    ]
    pinput = ""
    while pinput != "quit":
        pinput = input("COMMAND> ")
        if pinput not in commands:
            print("I don't understand your command")
        elif pinput == "look":
            print("Looking around!")
        elif pinput == "move":
            print("Moving to a place!")
        elif pinput == "help":
            print("Please use one of the following commands:")
            for command in commands:
                print(command)
        elif pinput == "inventory":
            print("You are holding a thing!")
