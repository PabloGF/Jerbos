#!/usr/bin/python

import os
import sys
import time

from twython import Twython


mensaje = 'Auto-tweet de #JerberryPi (Foto de hace una hora) [Comedor-Gimnasio]'


CONSUMER_KEY = 'XXXX'
CONSUMER_SECRET = 'XXXX'
ACCESS_KEY = 'XXXX'
ACCESS_SECRET = 'XXXX'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

foto = open('/home/pi/jerbos1.JPG', 'rb')

api.update_status_with_media(status= mensaje, media=foto)

print "Tweet enviado"

sys.exit()
