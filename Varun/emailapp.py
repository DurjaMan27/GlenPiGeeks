from tkinter import *
from tkinter import ttk

import smtplib
import webbrowser
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

def sendemail():
    try:

        # instance of MIMEMultipart
        msg = MIMEMultipart()
        
        sender = account.get()
        recepient = [receiver.get()]
        sub = subject.get()
        pswrd = password.get()
        #msg = msgbody.get('1.0','end')
        #msgtosend = """\
        #From: %s
        #To: %s
        #Subject: %s
        #
        #%s
        #""" % (sender, recepient, sub, msg)
        msg['From'] = sender
        msg['Subject'] = sub
        msg['To'] = recepient
        print(msg.as_string())
        content=msgbody.get('1.0', 'end')
        msg.attach(MIMEText(content, 'plain'))
        filename = "File_name_with_extension"
        attachment = open("/home/pi/GlenPiGeeks/gmailtest.py", "rb")
        print(msg.as_string())
        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 
  
        # encode into base64 
        encoders.encode_base64(p) 
   
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
        # attach the instance 'p' to instance 'msg' 
        msg.attach(p)
        msgtosend = msg.as_string()
        print(msgtosend)
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.starttls()
        mail.login(sender, pswrd)
        #mail.sendmail(sender, recepient, msgtosend)
        print(msgtosend)
        mail.close()
        
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
msgbody = Text(mainframe, width=30, height=10)
msgbody.grid(column=4, row=7, sticky=(W, E))

ttk.Button(mainframe, text="Send Email", command=sendemail).grid(column=4,row=8,sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

account_entry.focus()

root.mainloop()

