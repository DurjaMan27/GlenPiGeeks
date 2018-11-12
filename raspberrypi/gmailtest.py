import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
s.ehlo()

username='glenpigeeks'
#email
password='WarringtonGlen18976'
#password
s.login(username, password)

replyto='glenpigeeks@gmail.com'
#where a reply to will go
sendto=['kittykatie126@gmail.com','ballerzfordays@gmail.com', 'yidaos@gmail.com', 'varunvellorerao@gmail.com', 'velloregrao@gmail.com', 'abtondapu@gmail.com', 'sam55wats@gmail.com', 'atondapu@gmail.com', 'ajjay87@gmail.com', 'yingli102016@gmail.com', 'diyahundiwala@gmail.com']
sendtoShow='me@me.com'
87#what shows on the email as send to
subject='Test from GPG'
content="Hello from Glen Pi Geeks!\nThis is our first successful email from our Python code.\n Glen Pi Geeks Group" #content
mailtext='From '+replyto+'\nTo: '+sendtoShow+'\n'
mailtext=mailtext+'Subject:'+subject+'\n'+content
#send the email
s.sendmail(replyto, sendto, mailtext)
#we are done
rslt=s.quit()
print('Sendmail result=' + str(rslt[1]))
