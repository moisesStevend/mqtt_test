#!/usr/bin/env python
import paho.mqtt.client as mqtt
import time
import serial
import json

def on_connect(client, userdata, flags, rc):
	print("Empezamos a conectarnos con calidad "+str(rc))

class Envio_plot(object):
    def __init__(self):
        try:
            self.client = mqtt.Client(transport='websockets')
            self.client.connect("test.mosquitto.org",8080,60)
            self.client.loop_start()
            self.client.on_connect = on_connect
        except:
            print "no se pudo conectar al broker"

    def publicar(self, topico,mensaje):
        self.client.publish(topico, mensaje)

    def terminar(self):
        self.client.disconnect()
        
try:
	mi_envio=Envio_plot()
	ser=serial.Serial("/dev/ttyACM0",9600)
	mapeo=[]
	
	while 1:
		lect=ser.readline().split(":")
		lect=(float(lect[0]),int(lect[1]))
		
		if(len(mapeo)==10):
			mapeo.pop(0)
			mapeo.append(lect)
		else:
			mapeo.append(lect)
			
		mi_envio.publicar('data_sin', json.dumps(mapeo))
except:
	print "No se conecto"


	
