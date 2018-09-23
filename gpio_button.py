from gpiozero import Button

button = Button(2)

while True:
    button.wait_for_press()
    print('You pushed me')
