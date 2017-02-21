#!/usr/bin/env python

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  print("Empezamos a conectarnos con calidad "+str(rc))
  client.subscribe("diapos")

def on_message(client, userdata, msg):
  print msg.payload
  #if (msg.payload == "finish"):
  #  print("acabo!")
  #  client.disconnect()
    
client = mqtt.Client(transport='websockets')
#client.connect("test.mosquitto.org",8080,60)
client.connect("10.10.50.58",9001,60)

client.loop_start()

client.on_connect = on_connect
client.on_message = on_message

while True:
	men = raw_input('ingrese: ')
	#if men=='envio':
	client.publish("presence", men);
	#elif men=='salir':
	#	client.publish("display1", 'finish');
	#	break

client.loop_stop()
client.disconnect()
#client.loop_forever()
