#!/usr/bin/env python
import paho.mqtt.client as mqtt
from numpy import sin,pi,array, arange, deg2rad
import matplotlib.pyplot as plt
import time
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
        

		#self.client.subscribe("diapos")

def par(x,y):
	return (x,y)

inicio=0.0
#final=10.0
final=360.0
mi_envio=Envio_plot()

#time.sleep(5)

while(1):
	x=list(arange(deg2rad(inicio),deg2rad(final),0.05))
	y=list(sin(array(x)))

	#plt.plot(x,y)
	#plt.show()
	mapeo=map(par,x,y)
	#print json.dumps(mapeo)
	mi_envio.publicar('data_sin', json.dumps(mapeo))
	
	inicio+=5
	final+=5

	#stop
	#print x,y 
	#time.sleep(5)

'''
d=[14,25,23,4,25,36,27,18,29]
vv=[]

for i in range(len(d)):
	#print i,d[:(i+1)]
	x=d[:(i+1)]
	y=list(sin(2*pi*array(x)))
	
	#print x,y
		
	vv.append("'x':"+ str(x[i])+", 'y':"+str(y[i]))

print vv	
	
	#v.append("'x':{dx[0]}, 'y':{dy[0]}".format(dx=x, dy=y))
	#d=[]print v
'''
