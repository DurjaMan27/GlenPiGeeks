from sense_hat import SenseHat
import time
from datetime import date
from time import sleep
import io, time, os, sys, picamera, pygame

today = date.today()
sense = SenseHat()

# Twitter application authentication
APP_KEY = 'X0X3V2Ui6cY3WHmZn16K03cUy'
APP_SECRET = 'X0P9KWWggyvwr0OVzaH5rFwifSAVGeDPhqsoG9CRVzschmZzrJ'
OAUTH_TOKEN = '851088958050193409-LP01tcFrtS6z1dfUgiCuCExqN2PiPmq'
OAUTH_TOKEN_SECRET = '6DjSlW8ocWWuzRvNzrUQxYmU4JooYnfKxZh5PGtIft2LA'

from twython import Twython

twitter = Twython(
    APP_KEY,
    APP_SECRET,
    OAUTH_TOKEN,
    OAUTH_TOKEN_SECRET
    )

t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()
t = round(t, 1)
p = round(p, 1)
h = round(h, 1)
if t > 21.1 and t < 32.2:
    bg = [0, 100, 0] #green
else:
    bg = [100, 0, 0] #red      



 
# Display warning for deprecated Picamera functions (since v1.8) / affiche alerte si une fonction depreciee est utilisee 
import warnings
warnings.filterwarnings('default', category=DeprecationWarning)
 
pics_taken = 0
vid_taken = 0
 
# Init pygame and screen / initialise pygame et ecran
pygame.init()
res = pygame.display.list_modes() # return the resolution of your monitor / resolution du moniteur
width, height = res[0] # In case of trouble, set manually the resolution with: width, height = 1650, 1050
print ("Screen resolution :", width, "x", height)
screen = pygame.display.set_mode([width, height])
pygame.display.toggle_fullscreen()
pygame.mouse.set_visible = False
 
# Picamera object / objet Picamera
camera = picamera.PiCamera()
#camera.resolution = (1280, 720)
camera.framerate = float(24)
 
# Define functions / fonctions
def take_pic():
    global pics_taken
    pics_taken += 1
    camera.capture('image_' + str(pics_taken) + '.jpg')
    #msg = "Temperature = {0}, Pressure {1}, Humidity {2}".format (t,p,h)
    message = "Today is {3}. In Warrington, PA, Temperature = {0} °C, Pressure {1}, Humidity {2} @Raspberry_Pi @CBMillCreek #SenseHat".format (t,p,h,today)
    print (message)
    photo = open('/home/pi/Vrn Pi Prjt/image_1.jpg', 'rb')
    response = twitter.upload_media(media=photo)
    twitter.update_status(status=message, media_ids=[response['media_id']])
    #twitter.update_status(status=message)
    #sys.exit(0)
     
def quit_app():
    camera.close()
    pygame.quit()
    print ("You've taken", pics_taken, " pictures ", vid_taken, " videos. Don't forget to back them up (or they'll be overwritten next time)")
    sys.exit(0)
    
 
#Start camera preview / Demarre affichage en direct
camera.start_preview()
 
while(True):
  pygame.display.update()
  for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          quit_app()
          #to leave the preview click the escape key
        elif event.key == pygame.K_SPACE:
          take_pic()
          #to take a picture press the spacebar
        elif event.key == pygame.K_TAB:
           camera.start_preview()
