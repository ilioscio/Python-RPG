def bootGame():
    print("Welcome to Python RPG!")
    nameChoice = input("Please give a character name: ")
    print("Please choose a class")
    classChoice = int(input("1=warrior 2=ranger 3=wizard: "))
    while classChoice not in [1,2,3]:
        classChoice = int(input("Please choose either 1, 2, or 3: "))
    return(nameChoice,classChoice)
