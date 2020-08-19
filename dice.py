from random import choice

options = [i for i in range(1,7)]
print("Welcome to the dice game!")
intention = raw_input("Enter 'y' to roll!\n")

if intention != "y":
    exit()
else:
    while intention == "y":
        for _ in range(1):
            roll = choice(options)
            print("Nice! You got {}. Enter 'y' to roll again!".format(roll))
            intention = raw_input()
            break
        else:
            exit()
