
##from sense_hat import SenseHat
##import time
##
##sense = SenseHat()
##
##sense.show_message("Hello my name is Varun and this is SenseHat:-)", scroll_speed=0.05, text_colour=[0, 0, 255])
##
##
from twython import Twython
from twython import TwythonStreamer
from sense_hat import SenseHat
import time

# Twitter application authentication
APP_KEY = 'X0X3V2Ui6cY3WHmZn16K03cUy'
APP_SECRET = 'X0P9KWWggyvwr0OVzaH5rFwifSAVGeDPhqsoG9CRVzschmZzrJ'
OAUTH_TOKEN = '851088958050193409-LP01tcFrtS6z1dfUgiCuCExqN2PiPmq'
OAUTH_TOKEN_SECRET = '6DjSlW8ocWWuzRvNzrUQxYmU4JooYnfKxZh5PGtIft2LA'

sense = SenseHat
sense.show_message("Hello my name is Varun and this is SenseHat:-)", scroll_speed=0.05, text_colour=[0, 0, 255])


class MyStreamer(TwythonStreamer):

    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text'].encode('utf-8')
            print("@%s: %s" % (username, tweet))
            print(tweet)
            raise ValueError(tweet)
            
##try:
##    stream = MyStreamer(
##        APP_KEY,
##        APP_SECRET,
##        OAUTH_TOKEN,
##        OAUTH_TOKEN_SECRET
##        )
##
##    stream.statuses.filter(track='#Egypt')
##    
##except ValueError as err:

    
    
    
