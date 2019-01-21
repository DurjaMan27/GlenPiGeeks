from sense_hat import SenseHat
import time
from datetime import date
from time import sleep

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
#msg = "Temperature = {0}, Pressure {1}, Humidity {2}".format (t,p,h)
message = "Today is {3}. In Warrington, PA, Temperature = {0} °C, Pressure {1}, Humidity {2} @Raspberry_Pi @CBMillCreek #SenseHat".format (t,p,h,today)
print (message)
#twitter.update_status(status=message)

#sphoto = open('/home/pi/Vrn Pi Prjt/image_1.jpg', 'rb')
response = twitter.upload_media(media=photo)
#twitter.upload_media(media=photo)
#print(twitter.__version__)
#twitter.update_status(status=message, media_ids=[response['media_id']])
    
