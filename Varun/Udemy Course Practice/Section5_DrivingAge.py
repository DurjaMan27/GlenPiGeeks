#Section5_DrivingAge.py

driving_age = int(input("What is the legal driving age where you live? "))
your_age = int(input("How old are you? "))
name = input("What is your name? ")

#if your_age >= driving_age:
    #print("You are old enough to drive!")
#if your_age <= driving_age:
   # print("Sorry, you cannot drive right now. You will be able to drive in", driving_age - your_age, "years.")
if your_age >= driving_age:
    print(name, ", you are old enough to drive!")
else:
    print("Sorry", name,", you will be old enough to drive in", driving_age - your_age, "years.")