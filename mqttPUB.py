import paho.mqtt.client as paho
import time


def on_publish(client, userdata, mid):
    print("mid: " + str(mid))


client = paho.Client()
client.on_publish = on_publish
client.connect("broker.mqttdashboard.com", 1883)
#client.connect("broker.hivemq.com", 1883)
client.loop_start()

while True:
    msg = raw_input("enter something : ")
    (rc, mid) = client.publish("rohit/iot", str(msg), qos=1)
    print rc