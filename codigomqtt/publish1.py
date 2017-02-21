import paho.mqtt.client as paho
import time
 
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

client = paho.Client()
client.on_publish = on_publish
client.connect("iot.eclipse.org", 1883)
client.loop_start()
 
while True:
    msj = raw_input('valor a transmitir: ')
    client.publish("display/", msj, qos=1)
    time.sleep(30)
