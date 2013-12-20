#!/usr/bin/python

import os
import sys
import time
import commands
from twython import Twython

output=commands.getoutput('temp')
medida=output.split()[-1]
mensaje = 'Auto-tweet de #JerberryPi.[Nido-WC-Bebedero] La temperatura de los bichos es %s C' % medida


CONSUMER_KEY = 'XXXX'
CONSUMER_SECRET = 'XXXX'
ACCESS_KEY = 'XXXX'
ACCESS_SECRET = 'XXXX'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

foto = open('/home/pi/jerbos.JPG', 'rb')

api.update_status_with_media(status= mensaje, media=foto)

print "Tweet enviado"

sys.exit()
