# print("Hello World!")

# YourName.py
# name = input("What is your name?\n")
#print("Hi, ", name)

# YourNamex5.py
# name = input("What is your name?\n")
# print("Hi, ", name, name, name, name, name)

# MadLib.py
#adjective = input("Please enter an ajective: ")
#noun = input("Please enter a noun: ")
#verb = input("Please enter a verb ending in -ed: ")
#print("Your MadLib:")
#print("The", adjective, noun, verb, "at the crazy glen pi geekers.")

# LoopsPractice
#print(list(range(5)))

#RandomGames
#import random
#print(random.randint(1,15))

#GuessingGame.py
import random
the_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
while guess != the_number:
    if guess > the_number:
        print(guess, "was too high. Try again.")
    if guess < the_number:
        print(guess, "was too low. Try again.")
    guess = int(input("Guess again: "))
print(guess, "was the number! You win!")


# OldEnoughOrElse.py
driving_age = eval(input("What is the legal driving age where you live? "))
your_age = eval(input("How old are you? "))
if your_age >= driving_age:
    print("You're old enough to drive!")
else:
    print("Sorry, you can drive in", driving_age - your_age, "years.")
    


# PingPong_Calculator.py

def convert_in2cm(inches):
    return inches * 2.54
def convert_lb2kg(pounds):
    return pounds / 2.2

height_in = int(input("Enter your height in inches: "))
weight_lb = int(input("Enter your weight in pounds: "))

height_cm = convert_in2cm(height_in)
weight_kg = convert_lb2kg(weight_lb)

ping_pong_tall = round(height_cm / 4)
ping_pong_heavy = round(weight_kg * 1000 / 2.7)

feet = height_in // 12
inch = height_in % 12

print("At", feet, "feet", inch, "inches tall, and", weight_lb, 
      "pounds,")
print("you measure", ping_pong_tall, "Ping-Pong balls tall, and ")
print("you weigh the same as", ping_pong_heavy, "Ping-Pong balls!")