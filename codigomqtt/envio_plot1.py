#!/usr/bin/env python
from numpy import arange, sin, pi
import paho.mqtt.client as mqtt
import json

class Envio_plot(object):
    def __init__(self):
        try:
            self.client = mqtt.Client()
            self.client.connect("test.mosquitto.org",1883,60)
        except:
            print "no se pudo conectar al broker"

    def publicar(self, topico,mensaje):
        self.client.publish(topico, mensaje)

    def terminar(self):
        self.client.disconnect()

def conv(mi_x,mi_y):
    #acum=[{}]
    send = {
        'name': 'ploteo',
        'values': [{'x': mi_x, 'y': mi_y}],
        'strokeWidth': 3,
        'strokeDashArray': "5.5",
    }
    return json.dumps(send)
t=0
mi_envio=Envio_plot()
while(1):
    t=t+0.01
    mi_envio.publicar('presence',conv(t,sin(2*pi*t)))
    if(t==0.05):
        break
mi_envio.terminar()
'''
{
name: 'data1',
values: [ { x: 0, y: 20 }, { x: 1, y: 30 }, { x: 2, y: 10 }, { x: 3, y: 5 }, { x: 4, y: 8 }, { x: 5, y: 15 }, { x: 6, y: 10 },{ x: 10, y: 5 } ],
strokeWidth: 3,
strokeDashArray: "5,5",
},
'''
