import paho.mqtt.client as paho


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code % d." % (rc))

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_connect = on_connect
client.connect("broker.mqttdashboard.com", 1883)
#client.connect("broker.hivemq.com", 1883)
client.subscribe("test/temperature", qos=0)

client.loop_forever()