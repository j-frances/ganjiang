#!/usr/bin/python
# -*- coding: utf-8 -*-
# print u'你猜怎么着?'.encode('utf-8')
from random import randint
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

result = []
intention = 'y'
options = [i for i in range(1, 100)]

def clear():
    print(chr(27) + "[2J")

for _ in range(1):
    roll = randint(0, 100)
    result.append("{}".format(roll))

while intention:
    if intention == "y":
        guess = 0
        print("What is your guess?")
        while guess == 0:
            try:
                guess = int(input())
            except ValueError:
                print("Please input your guess as a whole number.")
                guess = 0
                break
        else:
            if int(result[0]) == guess:
                print("Correct!")
                exit()
            else:
                print("You guessed {} but the right answer was {}. Sorry!".format(guess, result[0]))
                intention = input("Enter 'y' to play again or 'q' to quit!.\n")
    else:
        if intention == "q":
            clear()
            exit()
        else:
            intention = input()
