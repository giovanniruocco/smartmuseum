import paho.mqtt.publish as publish
import json
import random
import time

popularity = 0
i = 0

while True:
    file = open("C:\\Users\\Giovanni\\Desktop\\GroupProject\\test.txt", "r")
    x = file.read()
    x = x.split("\n")
    print(x[-2])
    

    data="{\"devName\":\"LookAtME\"," + " \"ID\":1, " + (x[-2]) + "}" #create JSON object
    
    time.sleep(1)
    print(data)
    publish.single("tb/mqtt-integration/sensors", data, hostname="broker.hivemq.com", port=1883)