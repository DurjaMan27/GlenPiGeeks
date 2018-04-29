from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.show_letter("O", text_colour=[255, 0, 0])
sleep(1)
sense.show_letter("M", text_colour=[0, 255, 0])
sleep(1)
sense.show_letter("G", text_colour=[0, 0, 255])
sleep(1)
sense.show_letter("!", text_colour=[255, 0, 127], back_colour=[0, 0, 200])
sleep(1)
sense.clear()