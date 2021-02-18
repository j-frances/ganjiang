from random import choice
from sys import version_info
if version_info.major == 3:
    pass
elif version_info.major == 2:
    try:
        input = raw_input
    except NameError:
        pass
else:
    print("Unknown python version - input function not safe")

options = [i for i in range(1, 7)]
print("Welcome to the dice game!")
intention = input("Enter 'y' to roll!\n")
while intention:
    if intention == "y":
        for _ in range(1):
            roll = choice(options)
            print("Nice! You got {}. Enter 'y' to roll again!".format(roll))
            intention = input()
            break
