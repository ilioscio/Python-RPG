from random import randint
def bootGame():
    print("Welcome to Python RPG!")
    stats = []
    rstr = randint(1,10)
    stats.append(rstr)
    rdex = randint(1,10)
    stats.append(rdex)
    rint = randint(1,10)
    stats.append(rint)
    rvit = randint(1,10)
    stats.append(rvit)
    print("Rolled random stats: {} str, {} dex, {} int, {} vit".format(rstr,rdex,rint,rvit))
    nameChoice = input("Please give a character name: ")
    print("Please choose a class")
    classChoice = int(input("1=warrior 2=ranger 3=wizard: "))
    while classChoice not in [1,2,3]:
        classChoice = int(input("Please choose either 1, 2, or 3: "))
    return(nameChoice,classChoice,stats)
