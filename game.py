"""A number-guessing game."""

# Put your code here
from random import randint

def guess_the_num():
    top_limit = 100
    bottom_limit = 1
    count = 0
    num_in_mind = randint(bottom_limit, top_limit)
    guessed_num = 0

    guesser_name = input("Howdy, what is your name? (type in your name) ")
    print("{}, I'm thinking of a number between 1 and 100.".format(guesser_name))
    print("Try to guess my number. ")

    while guessed_num != num_in_mind:
        guessed_num = int(input("Your guess? "))
        
        if guessed_num < bottom_limit or guessed_num > top_limit:
            print("Your guess is out of range, try again.")
            continue

        if guessed_num < num_in_mind:
            print("Your guess is too low, try again.")
            bottom_limit == guessed_num
            count = count + 1
        elif guessed_num > num_in_mind:
            print("Your guess is too high, try again.")
            top_limit == guessed_num
            count = count + 1
        else:
            count = count + 1
            print("Well done, {}! You found my number in {} tries!".format(guesser_name, count))

guess_the_num()