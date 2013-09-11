#!/usr/bin/python
import subprocess
import smtplib
import socket

import mimetypes

from email.mime.text import MIMEText

from email.MIMEMultipart import MIMEMultipart 
from email.MIMEImage import MIMEImage 
from email.Encoders import encode_base64


import datetime
import commands
# Change to your own account information
to = 'xxxx@gmail.com'
gmail_user = 'zzzz@gmail.com'
gmail_password = 'yyyy'
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()


output=commands.getoutput('curl ifconfig.me')
ipaddr=output.split()[-1]
my_ip = 'Esta es la sala ahora mismo'
msg = MIMEMultipart(my_ip)
msg['Subject'] = 'Autofoto RasPi'
msg['From'] = gmail_user
msg['To'] = to

file = open("/home/pi/jerbos.JPG", "rb") 
attach_image = MIMEImage(file.read()) 
attach_image.add_header('Content-Disposition', 'attachment; filename = "/home/pi/jerbos.PNG"') 
msg.attach(attach_image)

smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
