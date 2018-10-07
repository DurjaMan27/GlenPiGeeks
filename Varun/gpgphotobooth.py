from tkinter import *
from tkinter import ttk
import picamera
from time import sleep

import smtplib
import webbrowser
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

camera = picamera.PiCamera()

def CameraON():
    camera.preview_fullscreen=False
    camera.preview_window=(90,100, 320, 240)
    camera.resolution=(640,480)
    camera.start_preview()
    
def CameraOFF():
    camera.stop_preview()
    
def CameraTakePic():
    camera.capture('/home/pi/GlenPiGeeks/PiPhotoBoothPictures/image.jpg')
    
def EXIT():
    root.destroy
    camera.stop_preview()
    camera.close()
    quit()

def sendemail():
    try:

       
        sender = account.get()
        recepient = [receiver.get()]
        sub = subject.get()
        pswrd = password.get()
        msgcontent = msgbody.get()
        # instance of MIMEMultipart
        msg = MIMEMultipart()

        #initialize SMTP Library
        s = smtplib.SMTP('smtp.gmail.com', 587)

        #initialize connection
        s.starttls()
        s.ehlo()
        s.login(sender, pswrd)

        # storing the senders email address   
        msg['From'] = str(sender) 
          
        # storing the subject  
        msg['Subject'] = str(sub)
          
        # storing the receivers email address  
        msg['To'] = str(recepient)

        # attach the body with the msg instance 
        msg.attach(MIMEText(str(msgcontent), 'plain'))
        print(msgcontent)
        #print(msg.as_string())
        #6 Insert the picture file
        # open the file to be sent  
        filename = "yourpicture.jpg"
        attachment = open("/home/pi/GlenPiGeeks/PiPhotoBoothPictures/image.jpg", "rb")

        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 
          
        # encode into base64 
        encoders.encode_base64(p) 
           
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
          
        # attach the instance 'p' to instance 'msg' 
        msg.attach(p)

        # Converts the Multipart msg into a string 
        text = msg.as_string()           

        #print(text)
        #send the email
        s.sendmail(sender,recepient, text)

        #we are done
        rslt=s.quit()
        print('Sendmail result=' + str(rslt[1]))
        
        ttk.Label(mainframe, text="Email sent successfully").grid(column=4,row=9,sticky=W)

    except Exception as e:
        ttk.Label(mainframe, text=str(e)).grid(column=4,row=9,sticky=W)
        print(str(e))

def setup(event):
    webbrowser.open_new(r"https://www.google.com/settings/security/lesssecureapps")
    
        
root = Tk()
root.title("Send an Email via Gmail !!")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.grid(row=5, column=4, columnspan=2)
mainframe.grid(row=6, column=4, columnspan=2)

ttk.Button(mainframe, text='Start Camera', command=CameraON).grid(row=8, column = 1)
ttk.Button(mainframe, text='Kill Camera', command=CameraOFF).grid(row=8, column = 2)
ttk.Button(mainframe, text='Exit Program', command=EXIT).grid(row=8, column = 3)
ttk.Button(mainframe, text='Take Picture', command=CameraTakePic).grid(row=8, column = 4)

account = StringVar()
password = StringVar()
receiver = StringVar()
subject = StringVar()
msgbody = StringVar()

a = Label(mainframe, text="To use this app turn this setting ON for your account", fg="blue", cursor="hand2")
a.grid(columnspan=2,column=3, row=0, sticky=W)
a.bind("<Button-1>", setup)


ttk.Label(mainframe, text="Your Email Account: ").grid(column=0, row=1, sticky=W)
account_entry = ttk.Entry(mainframe, width=30, textvariable=account)
account_entry.grid(column=4, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Your Password: ").grid(column=0, row=2, sticky=W)
password_entry = ttk.Entry(mainframe, show="*", width=30, textvariable=password)
password_entry.grid(column=4, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Recepient's Email Account: ").grid(column=0, row=3, sticky=W)
receiver_entry = ttk.Entry(mainframe, width=30, textvariable=receiver)
receiver_entry.grid(column=4, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Let's Compose").grid(column=2, row=5, sticky=W)

ttk.Label(mainframe, text="Subject: ").grid(column=0, row=6, sticky=W)
subject_entry = ttk.Entry(mainframe, width=30, textvariable=subject)
subject_entry.grid(column=4, row=6, sticky=(W, E))

ttk.Label(mainframe, text="Message Body: ").grid(column=0, row=7, sticky=W)
msgbody_entry = ttk.Entry(mainframe, width=30, textvariable=msgbody)
msgbody_entry.grid(column=4, row=7, sticky=(W, E))

ttk.Button(mainframe, text="Send Email", command=sendemail).grid(column=4,row=9,sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

account_entry.focus()

root.mainloop()

