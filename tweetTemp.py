#!/usr/bin/python

import os
import sys
import time

from twython import Twython


mensaje = '(BETA). Auto-tweet de #JerberryPi. Vaya Noche!'


CONSUMER_KEY = 'XXXX'
CONSUMER_SECRET = 'XXXX'
ACCESS_KEY = 'XXXX'
ACCESS_SECRET = 'XXXX'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

foto = open('/usr/bin/temp.png', 'rb')

api.update_status_with_media(status= mensaje, media=foto)

print "Tweet enviado"

sys.exit()
