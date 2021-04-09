#!/usr/bin/env python3

import logging
from logging.handlers import TimedRotatingFileHandler
from paho.mqtt.client import Client
import paho.mqtt.publish as publish
import uuid
import os
import pyodbc
import json
import pandas as pd
import smtplib
from datetime import datetime

########################################################################################################################
#  LOGGING SETUP
logging.basicConfig(level=logging.INFO, format='%(asctime)s,%(levelname)s,%(message)s', datefmt="%Y-%m-%d %H:%M:%S",
                    handlers=[TimedRotatingFileHandler(f'/home/pi/Source/Bleb/logs/daily.log', when='midnight', backupCount=5)])

client = Client()
client.on_message = lambda client, userdata, message: print(
    message.payload.decode())
client.connect('localhost')
client.subscribe([("gw_esp/FDB72ADBA9/000102030400/cmd", 2),
                 ("gw_esp/FDB72ADBA9/0001020304/cmd", 2), ("gw_esp/FAD4B9DDCA/FDB72ADBA9/data", 2)])

client.loop_forever()
