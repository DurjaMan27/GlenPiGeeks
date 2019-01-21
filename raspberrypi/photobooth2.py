from sense_hat import SenseHat
from picamera import PiCamera
from time import sleep

sense = Sensehat()
camera = PiCamera()
button = Button()

camera.start_preview()
sense.show_letter("3")
sleep(1)
sense.show_letter("2")
sleep(1)
sense.show_letter("1")
sleep(1)

camera.capture('home/pi/GlenPiGeeks/PiPhotoBoothPictures/image.jpg')
sense.show_message('1/3', text color = [0,255,255])
sleep(2)
camera.end_preview()
sense.clear()
sleep(1)

camera.start_preview()
sense.show_letter("3")
sleep(1)
sense.show_letter("2")
sleep(1)
sense.show_letter("1")
sleep(1)

camera.capture('home/pi/GlenPiGeeks/PiPhotoBoothPictures/image.jpg')
sense.show_message('1/3', text color = [0,255,255])
sleep(2)
camera.end_preview()
sense.clear()
sleep(1)

camera.start_preview()
sense.show_letter("3")
sleep(1)
sense.show_letter("2")
sleep(1)
sense.show_letter("1")
sleep(1)

camera.capture('home/pi/GlenPiGeeks/PiPhotoBoothPictures/image.jpg')
sense.show_message('1/3', text color = [0,255,255])
sleep(2)
camera.end_preview()
sense.clear()
sleep(1)

sense.show_message("END")
sleep(0.5)
sense.clear()
sense.show_message("END")
sleep(0.5)
sense.clear()
sense.show_message("END")
sleep(0.5)
sense.clear()
sense.show_message('Thank you for using the Glen Pi Geeks RPG! Please come again!', [0,255,0])
sleep(2)
sense.clear()

import smtplib

#initialize SMTP Library
s = smtplib.SMTP('smtp.gmail.com', 587)

#initialize connection
s.starttls()
s.ehlo()

#username
username='glenpigeeks'

#password
password='WarringtonGlen18976'

#login using username password
s.login(username, password)

#where a reply to will go
replyto='glenpigeeks@gmail.com'

#1 Change the subject to "your photo booth pictures from GPG
subject='Your Photo Booth Picture from Glen Pi Geeks!'

#2 send it only to the email of who is in the picture
sendto=['persontakingthepicture@gmail.com']
sendtoShow='me@me.com'

#3 name the file in a specific place
# write the code here

#4 date and time stamp the email address on the sheet
#there is no code

#5 Change the content "Thank you for taking the picture with us"
content="Hello from Glen Pi Geeks!\nAttached is your picture taken by our photo booth.\n Glen Pi Geeks Group" #content

#6 Insert the picture file
#write the code

#7 Include Marketing in the body of the email
#write the code

mailtext='From '+replyto+'\nTo: '+sendtoShow+'\n'
mailtext=mailtext+'Subject:'+subject+'\n'+content


#send the email
s.sendmail(replyto, sendto, mailtext)

#we are done
rslt=s.quit()
print('Sendmail result=' + str(rslt[1]))
