import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()

#create email
message = """Hi PiGeeks! This is Varun trying to send an email and picture from PiCamera and Raspberry Pi"""
msg.attach(MIMEText(message, 'plain'))

filename = "image_1.jpg"
attachment = open("/home/pi/Vrn Pi Prjt/image_1.jpg", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)

part.add_header('Content-Disposition', "attachment;filename= %s" % filename)

msg.attach(part)

msg['subject'] = 'Rpi Test'
msg['from'] = 'warringtonpigeeks'
msg['to'] = 'varunvellorerao@gmail.com'

#send email
s = smtplib.SMTP('smtp.gmail.com', '587')
s.ehlo()
s.starttls()
s.ehlo()
s.login('warringtonpigeeks@gmail.com', 'wedahgeeks@warrington')
s.sendmail(msg['From'], msg['To'], msg.as_string())
print ('Email sent')
s.quit()
    
