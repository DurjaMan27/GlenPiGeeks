#GuessingGame.py

import random
number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10. "))

while guess != number:
    if guess > number:
        print("Your guess was too high!")
    if guess < number:
        print("Your guess was too low!")
    guess = int(input("Guess again: "))
print(guess, "was the right answer! Good job!")
