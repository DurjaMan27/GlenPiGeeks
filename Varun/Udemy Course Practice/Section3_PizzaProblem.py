# ask the person how many pizzas they want
number = eval(input("How many pizzas do you want? "))
# ask the person the cost of each pizza
cost_of_pizzas = eval(input("How much does each pizza cost? "))
# calculate the total cost of the pizzas as the subtotal
subtotal = number * cost_of_pizzas
# calculate the sales tax, at 6 percent
tax = subtotal * 0.06
# figure out the total amount including the taxes
total = tax + subtotal
# show the user this amount
print("Your total amount for this order is $", total, ". Enjoy!")