#!/usr/bin/env python3

import logging
from logging.handlers import TimedRotatingFileHandler
from paho.mqtt.client import Client
from datetime import datetime
import time

global lastCommandTime
lastCommandTime = None


def on_message(client, userdata, message):
    global lastCommandTime
    topic = message.topic
    message = message.payload.decode()
    if topic.split("/")[-1] == "cmd":
        logging.info(f"COMMAND,{topic}")
        lastCommandTime = datetime.now()
    else:
        if lastCommandTime != None:
            if (datetime.now() - lastCommandTime).total_seconds() / 60.0 < 10:
                logging.info(f"DATA,{topic}")


########################################################################################################################
#  LOGGING SETUP
logging.basicConfig(level=logging.INFO, format='%(asctime)s,%(levelname)s,%(message)s', datefmt="%Y-%m-%d %H:%M:%S",
                    handlers=[TimedRotatingFileHandler(f'/home/pi/Source/Bleb/logs/daily.log', when='midnight', backupCount=50)])

client = Client()
client.on_message = on_message
client.connect('localhost')
client.subscribe("gw_esp/FDB72ADBA9/000102030400/cmd")
client.subscribe("gw_esp/FDB72ADBA9/0001020304/cmd")
client.subscribe("gw_esp/FAD4B9DDCA/FDB72ADBA9/data")

client.loop_forever()
