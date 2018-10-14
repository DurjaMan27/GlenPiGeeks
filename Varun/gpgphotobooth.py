from tkinter import *
from tkinter import ttk
import picamera
from time import sleep
import subprocess
import smtplib
import webbrowser
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

camera = picamera.PiCamera()

def toggleKeyboard(entry_widget_1):
    p = subprocess.Popen(['florence show'], shell=True, stdout= subprocess.PIPE, stderr= subprocess.PIPE, universal_newlines=True)
    if not "" == p.stderr.readline():
        subprocess.Popen(['florence'], shell=True)
        
def CameraON():
    camera.preview_fullscreen=False
    camera.preview_window=(90,100, 320, 240)
    camera.resolution=(640,480)
    camera.start_preview()
    
def CameraOFF():
    camera.stop_preview()
    
def CameraTakePic():
    camera.annotate_text = "Happy Diwali from the Glen Pi Geeks!"
    #camera.annotate_text_size = 120
    camera.capture('/home/pi/GlenPiGeeks/PiPhotoBoothPictures/image.jpg')
    
def EXIT():
    root.destroy
    camera.stop_preview()
    camera.close()
    quit()

def sendemail():
    try:

       
        #sender = account.get()
        sender = "glenpigeeks@gmail.com"
        recepient = [receiver.get()]
        #sub = subject.get()
        sub = "Hello from Glen Pi Geeks!"
        #pswrd = password.get()
        pswrd = "WarringtonGlen18976"
        #msgcontent = msgbody.get()
        msgcontent = "Here is your picture! Thank you for stopping by Glen Pi Geeks Photo Booth"
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
        
        ttk.Label(mainframe, text="Email sent successfully").grid(column=0,row=8)

    except Exception as e:
        #ttk.Label(mainframe, text=str(e)).grid(column=4,row=9,sticky=W)
        print(str(e))

def setup(event):
    webbrowser.open_new(r"https://www.google.com/settings/security/lesssecureapps")
    
        
root = Tk()
root.title("Glen Pi Geeks Photobooth!!")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.grid(row=5, column=1, columnspan=2)
mainframe.grid(row=6, column=1, columnspan=2)

account = StringVar()
password = StringVar()
receiver = StringVar()
subject = StringVar()
msgbody = StringVar()

ttk.Label(mainframe, text="Recepient's Email Account: ").grid(column=0, row=1, sticky=W)
receiver_entry = ttk.Entry(mainframe, width=30, textvariable=receiver)
#receiver_entry.bind('<FocusIn>',toggleKeyboard)
receiver_entry.grid(column=0, row=2, sticky=(W, E))

ttk.Button(mainframe, text='Start Camera', command=CameraON).grid(row=3, column = 0)
ttk.Button(mainframe, text='Kill Camera', command=CameraOFF).grid(row=4, column = 0)
ttk.Button(mainframe, text='Exit Program', command=EXIT).grid(row=5, column = 0)
ttk.Button(mainframe, text='Take Picture', command=CameraTakePic).grid(row=6, column = 0)
ttk.Button(mainframe, text="Send Email", command=sendemail).grid(column=0,row=7)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

receiver_entry.focus()

root.mainloop()

