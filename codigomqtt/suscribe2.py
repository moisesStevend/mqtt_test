#!/usr/bin/env python

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  print("Empezamos a conectarnos con calidad "+str(rc))
  client.subscribe("outTopic")

def on_message(client, userdata, msg):
  print msg.payload
  if (msg.payload == "finish"):
    print("acabo!")
    client.disconnect()
    
client = mqtt.Client()
client.connect("localhost",1883,60)
#client.connect("test.mosquitto.org",1883,60)
client.loop_start()

client.on_connect = on_connect
client.on_message = on_message

while True:
	men = raw_input("mensaje: ")
	client.publish("inTopic", men)
	#if men=='envio':
	#	client.publish("presence", men);
	#elif men=='salir':
	#	client.publish("presence", 'finish');
    
	#break

client.loop_stop()
client.disconnect()
#client.loop_forever()


