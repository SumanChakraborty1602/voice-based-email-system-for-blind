import speech_recognition as sr
import smtplib
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
import imghdr
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Say the project name
print("Welcome to Voice based Email System for blind.")
tts = gTTS(text="Welcome to Voice based Email System for blind.", lang='en')
ttsname=("name.mp3") 
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
print("This Voice Based Email System has been Created by Suman Chakraborty.")
tts = gTTS(text="This Voice Based Email System has been Created by Suman Chakraborty.", lang='en')
ttsname=("name.mp3") 
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
#Login details From OS
login = os.getlogin
print ("You are logging from "+login()+" System")
#Your Choices
print ("1. Compose a mail.")
tts = gTTS(text="Option 1. Compose a mail.", lang='en')
ttsname=("hello.mp3") 
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
print ("2. Check your inbox.")
tts = gTTS(text="Option 2. Check your inbox.", lang='en')
ttsname=("second.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
tts = gTTS(text="What is your choice? Please Say", lang='en')
ttsname=("hello.mp3") 
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
#Google Speech Recognition 
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Listening...')
    audio=r.listen(source)
    print ("Choice Recognized.")
    tts = gTTS(text="Choice Recognized.", lang='en')
    ttsname=("hello.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
try:
    text=r.recognize_google(audio)
    print ("Your Choice is : "+text)
    tts = gTTS(text="You Choice is : "+text, lang='en')
    ttsname=("hello.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
except sr.UnknownValueError:
    print("I Couldn't understand,Please say it again.")
    tts = gTTS(text="I Couldn't understand,Please say it again.", lang='en')
    ttsname=("hello.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
except sr.RequestError as e:
    print("Google Speech Recognition service couldn't produce results; {0}".format(e)) 
    tts = gTTS(text="Google Speech Recognition service couldn't produce results; {0}", lang='en')
    ttsname=("hello.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
if text == '1' or text == 'One' or text == 'one'or text == 'first'or text == 'First'or text == 'option one'or text == 'Option one'or text == 'option 1'or text == 'option One':
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        #Receiver of the email
        print('Listening...')
        tts = gTTS(text="To whom you want to send email? Please Say the Email Address", lang='en')
        ttsname=("hello.mp3") 
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        audio=r.listen(source)
        print ("Receiver's Email Address Recognized.")
        tts = gTTS(text="Receiver's Email Address Recognized.", lang='en')
        ttsname=("hello.mp3") 
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
    try:
        text12=r.recognize_google(audio)
        print ("Receiver's Email Address is : "+text12)
        tts = gTTS(text="Receiver's Email Address is : "+text12, lang='en')
        ttsname=("hello.mp3") 
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        receiver = text12
    except sr.UnknownValueError:
        print("I Couldn't understand,Please say it again.")
        tts = gTTS(text="I Couldn't understand,Please say it again.", lang='en')
        ttsname=("hello.mp3") 
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
    except sr.RequestError as e:
        print("Google Speech Recognition service couldn't produce results; {0}".format(e))
        tts = gTTS(text="Google Speech Recognition service couldn't produce results; {0}", lang='en')
        ttsname=("hello.mp3") 
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
    with sr.Microphone() as source:
        #Subject of the email
        print('Listening...')
        tts = gTTS(text="What is the Subject of the email? Please Say", lang='en')
        ttsname=("hello.mp3") 
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        audio=r.listen(source)
        print ("Subject of the Email Recognized.")
        tts = gTTS(text="Subject of the Email Recognized.", lang='en')
        ttsname=("hello.mp3") 
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
    try:
        text13=r.recognize_google(audio)
        print ("Subject of the Email is : "+text13)
        tts = gTTS(text="Subject of the Email is : "+text13, lang='en')
        ttsname=("hello.mp3") 
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        sub = text13
    except sr.UnknownValueError:
        print("I Couldn't understand,Please say it again.")
        tts = gTTS(text="I Couldn't understand,Please say it again.", lang='en')
        ttsname=("hello.mp3") 
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
    except sr.RequestError as e:
        print("Google Speech Recognition service couldn't produce results; {0}".format(e))
        tts = gTTS(text="Google Speech Recognition service couldn't produce results; {0}", lang='en')
        ttsname=("hello.mp3") 
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
    with sr.Microphone() as source:
        #Message of the email
        print('Listening...')
        tts = gTTS(text="What is your message? Please Say", lang='en')
        ttsname=("hello.mp3") 
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        audio=r.listen(source)
        print ("Message of the Email Recognized.")
        tts = gTTS(text="Message of the Email Recognized.", lang='en')
        ttsname=("hello.mp3") 
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
    try:
          text14=r.recognize_google(audio)
          print ("Your Message is : "+text14)
          tts = gTTS(text="Your Message is : "+text14, lang='en')
          ttsname=("hello.mp3") 
          tts.save(ttsname)
          music = pyglet.media.load(ttsname, streaming = False)
          music.play()
          time.sleep(music.duration)
          os.remove(ttsname)
          msg = text14
    except sr.UnknownValueError:
        print("I Couldn't understand,Please say it again.")
        tts = gTTS(text="I Couldn't understand,Please say it again.", lang='en')
        ttsname=("hello.mp3") 
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
    except sr.RequestError as e:
        print("Google Speech Recognition service couldn't produce results; {0}".format(e)) 
        tts = gTTS(text="Google Speech Recognition service couldn't produce results; {0}", lang='en')
        ttsname=("hello.mp3") 
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname) 
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo() #Hostname to send for this command defaults to the FQDN of the local host.
    mail.starttls() #security connection
    # Make sure to give app access in your Google account
    mail.login('Your Email Address','Password')
    #mesg = f'Subject: {sub}\n\n{msg}'
    mess= EmailMessage()
    #mess = MIMEMultipart()
    mess['From'] = 'Your Email Address'
    mess['To'] = receiver
    mess['Subject'] = sub
    mess.set_content(msg)
    files = ['Attachement file']
    for file in files:
        with open(file,'rb') as f:
           file_data = f.read()
           file_type = imghdr.what(f.name)
           file_name = f.name
        mess.add_attachment(file_data, maintype='image',subtype=file_type,filename=file_name)
    #mess.attach(MIMEText(msg, 'plain'))
    #attach_file_name = 'sample.pdf'
    #attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    #payload = MIMEBase('application', 'octate-stream')
    #payload.set_payload((attach_file).read())
   #encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename
    #payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    #mess.attach(payload)   
    #msg1 = mess.as_string()
    mail.send_message(mess)
    #mail.sendmail('Your Email Address','Receiver's Email Address',msg1)
    print ("Congrats! Your email has been sent. ")
    tts = gTTS(text="Congrats! Your email has been sent. ", lang='en')
    ttsname=("send.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    mail.close()   
if text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To'or text == 'Second' or text == 'second'or text == 'Option two'or text == 'Option tu'or text == 'Option to'or text == 'Option 2'or text == 'Option Two'or text == 'Option Tu'or text == 'Option To'or text == 'option two'or text == 'option to'or text == 'option tu'or text == 'option 2'or text == 'option Two'or text == 'Option Tu'or text == 'Option To':
    mail = imaplib.IMAP4_SSL('imap.gmail.com',993) #this is host and port area.... ssl security
    unm = ('Your Email Address')  #username
    psw = ('Password')  #password
    mail.login(unm,psw)  #login
    stat, total = mail.select('Inbox')  #total number of mails in inbox
    print ("Number of mails in your inbox :"+str(total))
    tts = gTTS(text="Total mails are :"+str(total), lang='en') #voice out
    ttsname=("total.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    #Unread emails
    unread = mail.search(None, 'Unread') # unread count
    print ("Number of Unread mails :"+str(unread))
    tts = gTTS(text="Your Unread mail :"+str(unread), lang='en')
    ttsname=("unseen.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    #Search emails
    result, data = mail.uid('search',None, "ALL")
    inbox_item_list = data[0].split()
    new = inbox_item_list[-1]
    old = inbox_item_list[0]
    result2, email_data = mail.uid('fetch', new, '(RFC822)') #fetch
    raw_email = email_data[0][1].decode("utf-8") #decode
    email_message = email.message_from_string(raw_email)
    print ("From: "+email_message['From'])
    print ("Subject: "+str(email_message['Subject']))
    tts = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
    ttsname=("mail.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    #Body part of emails
    stat, total1 = mail.select('Inbox')
    stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser")
    txt = soup.get_text()
    print ("Body :"+txt)
    tts = gTTS(text="Body: "+txt, lang='en')
    ttsname=("body.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    mail.close()
    mail.logout()