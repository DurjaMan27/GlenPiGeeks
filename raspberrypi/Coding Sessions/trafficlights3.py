from gpiozero import Button

button = Button(20)

while True:
    button.wait_for_press()
    print("Pressed")
    button.wait_for_release()
    print("Released")
    
