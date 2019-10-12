
# print("Hello World!")

# YourName.py
# name = input("What is your name?\n")
# print("Hi, ", name)

# YourNamex5.py
# name = input("What is your name?\n")
# print("Hi, ", name, name, name, name, name)

# MadLib.py
#adjective = input("Please enter an adjective: ")
#noun = input("Please enter a noun: ")
#verb = input("Please enter a verb ending in -ed: ")
#print("Your MadLib:")
#print("The", adjective, noun, verb, "at the Glen Pi Freaks.")

#String Practice
#name = input("What is your name? ")
#for x in range(35):
    #print(name, end = " is awesome! ")

# Loop Practice
#print(list(range(5)))

# GuessingGame.py
#import random
#the_number = random.randint(1, 100)
#guess = int(input("Guess a number between 1 and 100: "))
#while guess != the_number:
  #  if guess > the_number:
 #       print(guess, "was too high. Guess again.")
#    if guess < the_number:
        #print(guess, "was too low. Guess again.")
    #guess = int(input("Guess again: "))
#print(guess, "was the number! You win!")

#Rolling a Dice
import random
keep_going = True
while keep_going:
    # 'Roll' five random dice
    dice = [0,0,0,0,0]
    for i in range(5): # 'Roll'
        dice[i] = random.randint(1,6)
    print("You rolled:", dice)
    answer = input("Keep going?")
    keep_going = (answer == "")