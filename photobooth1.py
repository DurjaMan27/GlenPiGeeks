from sense_hat import SenseHat
from picamera import PiCamera
from time import sleep

sense = Sensehat()
camera = PiCamera()
button = Button()

camera.start_preview()
button.wait_for_press()
button.when_pressed = camera.capture('home/pi/GlenPiGeeks/image.jpg'), sense.show_letter('1', text colour = [0,255,255])
sleep(3)
camera.end_preview()
sense.clear()
sleep(2)

sense.show_letter("5")
sleep(1)
sense.show_letter("4")
sleep(1)
sense.show_letter("3")
sleep(1)
sense.show_letter("2")
sleep(1)
sense.show_letter("1")
sleep(1)
sense.clear()

camera.start_preview()
button.wait_for_press()
button.when_pressed = camera.capture('home/pi/GlenPiGeeks/image1.jpg'), sense.show_letter('2', text colour = [0,255,255])
sleep(3)
camera.end_preview()
sense.clear()
sleep(2)

sense.show_letter("5")
sleep(1)
sense.show_letter("4")
sleep(1)
sense.show_letter("3")
sleep(1)
sense.show_letter("2")
sleep(1)
sense.show_letter("1")
sleep(1)
sense.clear()

camera.start_preview()
button.wait_for_press()
button.when_pressed = camera.capture('home/pi/GlenPiGeeks/image2.jpg'), sense.show_letter('3', text colour = [0,255,255])
sleep(3)
camera.end_preview()
sense.clear()
sleep(2)

sense.show_message("END")
sleep(0.5)
sense.clear()
sense.show_message("END")
sleep(0.5)
sense.clear()
sense.show_message("END")
sleep(0.5)
sense.clear()
sense.show_message("Thank you for using the Glen Pi Geeks Raspberry Pi Photo Booth v1.0!)


#email part
