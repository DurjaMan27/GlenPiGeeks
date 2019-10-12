from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.start_recording('home/pi/video.h264')
sleep(10)
Camera.stop_recording()
Camera.stop_preview()




print('Hello')

