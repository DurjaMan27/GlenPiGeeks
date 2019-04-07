from time import sleep
import random
from random import choice

print("Hello, user. Welcome to this test. I will give you some random numbers and you'll have to answer them. It should be pretty easy. Or is it? Only one way to find out!")
sleep (5)

systems = ['Add', 'Subtract', 'Multiply', 'Divide']
print (choice(systems))

firstnumber = random.random() * 100
secondnumber = random.random() * 100
print(firstnumber)
print(secondnumber)
answer = firstnumber + secondnumber

guess = eval(input("What is the answer?"))
print("Your answer was", guess)
print("The real answer was", answer)

