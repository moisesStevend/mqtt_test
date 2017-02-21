#!/usr/bin/env python

import paho.mqtt.client as mqtt
import random 
import time

def gen_random():
	alm=[]
	for i in range(20):
		alm.append(random.random())
	return str(alm)

client = mqtt.Client()
client.connect("test.mosquitto.org",1883,60)

texto=''

with open('publish2.py','r') as f:
	texto=f.read()
f.closed

print texto

while True:
	texo_random=gen_random()
	#men = raw_input("mensaje: ")
	#if men=='envio':
	client.publish("display1", texo_random);
	#elif men=='salir':
	#	client.publish("display1", 'finish');
	#	break
	time.sleep(0.1)
client.disconnect();
