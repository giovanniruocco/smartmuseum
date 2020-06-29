import paho.mqtt.publish as publish
import json
import random
import time

popularity = 0
i = 0

while True:
    data="{\"devName\":\"LookAtME4\"," + " \"ID\":4, \"Trigger\": " + str(int(random.randrange(0,11)/10)) + ", \"Distance\": " + str(random.randrange(0,151)) + "}" #create JSON object

    time.sleep(1)
    print(data)
    publish.single("tb/mqtt-integration/sensors", data, hostname="broker.hivemq.com", port=1883)