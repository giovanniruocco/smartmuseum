import paho.mqtt.client as mqtt
import json
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("tb/mqtt-integration/tour")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    data = json.loads(msg.payload)

    if(data["ActivateClient2"] == 1):
        print("Lights on Statue 2")
        time.sleep(1)
        print('Playing recordings...')
        time.sleep(4)
        payload = "{\"devName\": \"Tour\", \"ActivateClient1\": 0, \"ActivateClient2\": 0, \"ActivateClient3\": 1 }"
        client.publish("tb/mqtt-integration/tour", payload)
        print("done.")



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()