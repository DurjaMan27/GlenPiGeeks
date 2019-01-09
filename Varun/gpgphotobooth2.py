from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
import picamera
from time import sleep
import subprocess
import smtplib
import webbrowser
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
from google.cloud.vision import types
from PIL import ImageDraw

# explain what these imports do
import argparse
import io
import re
import os

# explain what this environment variable does
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/GoogleCloudEval-e422de340b3a.json"

root = Tk()
root.title("GPG Photobooth 2.0!!")

camera = picamera.PiCamera()

# explain what detect_faces does 
# [START vision_face_detection]
def detect_faces(path):
    """Detects faces in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_face_detection]
    # [START vision_python_migration_image_file]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    # [END vision_python_migration_image_file]

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    
    detection = "faces:"
    for face in faces:
        print(type(face))
        #print(face.anger_likelihood)
        print(likelihood_name[face.anger_likelihood])
        print(face.sorrow_likelihood)
        print(face.joy_likelihood)
        print(face.surprise_likelihood)
        print(face.under_exposed_likelihood)
        print(face.blurred_likelihood)
        print(face.headwear_likelihood)
        if (likelihood_name[face.joy_likelihood]) == 'VERY_LIKELY' or  (likelihood_name[face.joy_likelihood]) == 'LIKELY':
            ShowEmotion("joy")
        elif (likelihood_name[face.joy_likelihood]) == 'POSSIBLE' :
            ShowEmotion("question")
        elif (likelihood_name[face.anger_likelihood]) == 'VERY_LIKELY' or (likelihood_name[face.anger_likelihood]) == 'LIKELY':
            ShowEmotion("anger")
        elif (likelihood_name[face.sorrow_likelihood]) == 'VERY_LIKELY' or (likelihood_name[face.sorrow_likelihood]) == 'LIKELY':
            ShowEmotion("sorrow")
        elif (likelihood_name[face.surprise_likelihood]) == 'VERY_LIKELY' or (likelihood_name[face.surprise_likelihood]) == 'LIKELY':
            ShowEmotion("surprise")
        elif (likelihood_name[face.blurred_likelihood]) == 'VERY_LIKELY' or (likelihood_name[face.blurred_likelihood]) == 'LIKELY':
            ShowEmotion("blurred")
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
        print('sorrow: {}'.format(likelihood_name[face.sorrow_likelihood]))
        print('blurred: {}'.format(likelihood_name[face.blurred_likelihood]))
        

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))
        #ttk.Label(mainframe, text=detection).grid(column=0,row=9)
        
    return faces

    # [END vision_python_migration_face_detection]
# [END vision_face_detection]

# [START vision_face_detection_tutorial_send_request]
def detect_face(face_file, max_results=4):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image).face_annotations
# [END vision_face_detection_tutorial_send_request]

def highlight_faces(image, faces, output_filename):
    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    for face in faces:
        box = [(vertex.x, vertex.y)
               for vertex in face.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')

    im.save(output_filename)

def toggleKeyboard(entry_widget_1):
    p = subprocess.Popen(['florence show'], shell=True, stdout= subprocess.PIPE, stderr= subprocess.PIPE, universal_newlines=True)
    if not "" == p.stderr.readline():
        subprocess.Popen(['florence'], shell=True)
        
def CameraON():
    camera.preview_fullscreen=False
    camera.preview_window=(90,100, 320, 240)
    camera.resolution=(640,640)
    #camera.brightness = 60
    camera.start_preview()
    
def CameraOFF():
    camera.stop_preview()
    
def CameraTakePic():
    #camera.annotate_text = "Welcome to Glen Pi Geeks Photo Booth 2.0 - Make a Face!"
    camera.capture('/home/pi/GlenPiGeeks/PiPhotoBoothPictures/image.png')
    load = Image.open("/home/pi/GlenPiGeeks/PiPhotoBoothPictures/image.png")
    load = load.resize((160, 160), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    mainframe.display = Label(mainframe,image=render)
    mainframe.display.image = render
    mainframe.display.grid(row=5, column=0)

def ShowEmotion(emotion):
    if emotion == "joy":
        load = Image.open("/home/pi/GlenPiGeeks/PiPhotoBoothPictures/joy.png")
    elif emotion == "anger":
        load = Image.open("/home/pi/GlenPiGeeks/PiPhotoBoothPictures/anger.png")
    elif emotion == "sorrow":
        load = Image.open("/home/pi/GlenPiGeeks/PiPhotoBoothPictures/sorrow.jpg")
    elif emotion == "headwear":
        load = Image.open("/home/pi/GlenPiGeeks/PiPhotoBoothPictures/headwear.png")
    elif emotion == "surprise":
        load = Image.open("/home/pi/GlenPiGeeks/PiPhotoBoothPictures/surprise.png")
    elif emotion == "question":
        load = Image.open("/home/pi/GlenPiGeeks/PiPhotoBoothPictures/question.jpg")
        ttk.Label(mainframe, text="Hmm...we can't detect your emotion, wanna try again?").grid(column=2,row=6)
    load = load.resize((160, 160), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    # labels can be text or images
    mainframe.display = Label(mainframe,image=render)
    mainframe.display.image = render
    mainframe.display.grid(row=5, column=2)
    
def AnalyzePic():
    detect_faces('/home/pi/GlenPiGeeks/PiPhotoBoothPictures/image.png')
    with open('/home/pi/GlenPiGeeks/PiPhotoBoothPictures/image.png', 'rb') as image:
        faces = detect_face(image, 4)
        print('Found {} face{}'.format(
            len(faces), '' if len(faces) == 1 else 's'))

        print('Writing to file {}'.format('/home/pi/GlenPiGeeks/PiPhotoBoothPictures/image1.png'))
        # Reset the file pointer, so we can read the file again
        image.seek(0)
        highlight_faces(image, faces, '/home/pi/GlenPiGeeks/PiPhotoBoothPictures/image1.png')
    load = Image.open("/home/pi/GlenPiGeeks/PiPhotoBoothPictures/image1.png")
    load = load.resize((160, 160), Image.ANTIALIAS) 
    render = ImageTk.PhotoImage(load)
    mainframe.display = Label(mainframe,image=render)
    mainframe.display.image = render
    mainframe.display.grid(row=5, column=1)
    
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
        attachment = open("/home/pi/GlenPiGeeks/PiPhotoBoothPictures/image.png", "rb")

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
        try:
            s.sendmail(sender,recepient, text)
        except SMTPRecipientsRefused:
            ttk.Label(mainframe, text="Email Recipients refused. Please try again with a proper email address.").grid(column=0,row=8)
            print("email recipients refused")
        except SMTPResponseException:
            ttk.Label(mainframe, text="Email Response Exception. Please try again with a proper email address.").grid(column=0,row=8)
            print("email response exception")
        except SMTPSenderRefused:
            ttk.Label(mainframe, text="Email Sender Refused. Please try again with a proper email address.").grid(column=0,row=8)
            print("email sender refused")
        except SMTPConnectError:
            ttk.Label(mainframe, text="Email Connect Error. Please try again with a proper email address.").grid(column=0,row=8)
            print("email connect error")
        except SMTPDataError:
            print("data error")
        except Exception as e:
            print(str(e))
        else: 
            #we are done
            rslt=s.quit()
            print('Sendmail result=' + str(rslt[1]))
            ttk.Label(mainframe, text="Email sent successfully").grid(column=0,row=6)
            print("quit email")
    except Exception as e:
        print(str(e))

def setup(event):
    webbrowser.open_new(r"https://www.google.com/settings/security/lesssecureapps")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.grid(row=5, column=1, columnspan=3)
mainframe.grid(row=6, column=1, columnspan=3)

account = StringVar()
password = StringVar()
receiver = StringVar()
subject = StringVar()
msgbody = StringVar()

ttk.Label(mainframe, text="Recepient's Email Account: ").grid(column=0, row=1, sticky=W)
receiver_entry = ttk.Entry(mainframe, width=30, textvariable=receiver)
receiver_entry.grid(column=1, row=1, sticky=(W, E))

ttk.Button(mainframe, text='Start Camera', command=CameraON).grid(row=3, column = 0)
ttk.Button(mainframe, text='Kill Camera', command=CameraOFF).grid(row=4, column = 0)
ttk.Button(mainframe, text='Take Picture', command=CameraTakePic).grid(row=3, column = 1)
ttk.Button(mainframe, text='Analyze Picture', command=AnalyzePic).grid(row=4, column = 1)
ttk.Button(mainframe, text="Send Email", command=sendemail).grid(row=3, column=2)
ttk.Button(mainframe, text='Exit Program', command=EXIT).grid(row=4, column = 2)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

receiver_entry.focus()

root.mainloop()

