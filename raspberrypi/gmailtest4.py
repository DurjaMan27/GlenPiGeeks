import smtplib

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders    

# instance of MIMEMultipart
msg = MIMEMultipart()

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

# storing the senders email address   
msg['From'] = replyto 
  
 

#1 Change the subject to "your photo booth pictures from GPG
subject='Your Photo Booth Picture from Glen Pi Geeks!'

# storing the subject  
msg['Subject'] = subject
  

#2 send it only to the email of who is in the picture
sendto='velloregrao@gmail.com'
sendtoShow='velloregrao@gmail.com'

# storing the receivers email address  
msg['To'] = sendto

#3 name the file in a specific place
# write the code here


#4 date and time stamp the email address on the sheet
#there is no code

#5 Change the content "Thank you for taking the picture with us"
content="Hello from Glen Pi Geeks!\nAttached is your picture taken by our photo booth.\n Glen Pi Geeks Group" #content
#attaching a file to the content area of the email
# attach the body with the msg instance 
msg.attach(MIMEText(content, 'plain'))

#6 Insert the picture file
# open the file to be sent  
filename = "File_name_with_extension"
attachment = open("/home/pi/GlenPiGeeks/gmailtest.py", "rb")

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p)

#7 Include Marketing in the body of the email
#write the code

mailtext='From '+replyto+'\nTo: '+sendtoShow+'\n'
mailtext=mailtext+'Subject:'+subject+'\n'+content

# Converts the Multipart msg into a string 
text = msg.as_string() 
  

print(text)


#send the email
s.sendmail(replyto, sendto, text)

#we are done
rslt=s.quit()
print('Sendmail result=' + str(rslt[1]))

