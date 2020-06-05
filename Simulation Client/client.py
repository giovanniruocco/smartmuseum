import paho.mqtt.client as mqtt
import json
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("tb/mqtt-integration/sensors")
    client.subscribe("tb/mqtt-integration/tour")

execution = False
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    data = json.loads(msg.payload)
    global execution

    if("Trigger" in data):
        if(data["Trigger"] == 1 and not execution):
            execution = True
            payload = "{\"devName\": \"Tour\", \"ActivateClient1\": 1, \"ActivateClient2\": 0, \"ActivateClient3\": 0 }"
            client.publish("tb/mqtt-integration/tour", payload)
            print("Lights on Statue 1")
            time.sleep(1)
            print('Playing recordings...')
            time.sleep(4)
            payload = "{\"devName\": \"Tour\", \"ActivateClient1\": 0, \"ActivateClient2\": 1, \"ActivateClient3\": 0 }"
            client.publish("tb/mqtt-integration/tour", payload)
            print("done.")

    if (("ActivateClient2" in data) and ("ActivateClient3" in data)): 
        if(data["ActivateClient2"]==0 and data["ActivateClient3"]==0): # if added new clients add new conditions
            execution = False


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
