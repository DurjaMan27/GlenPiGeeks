#StringFormatting.py

number = 2

num_width = len(bin(number)[2:])
space = " "
width = space * num_width
for i in range(0, number):
    print(width + int(1 + i) + width + oct((1 + i)[2:]) + width + hex((1 + i)[2:] + width + bin((1 + i)[2:]))