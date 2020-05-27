import paho.mqtt.subscribe as subscribe
import json
import time

def on_message_print(client, userdata, message):
    data = json.loads(message.payload)
    
    if (data['Trigger']==1) :
        print('Trigger!')
        time.sleep(3)
        print('Statue # 1')
        time.sleep(1)
        print('Turning on the Lights.')
        time.sleep(1)
        print('Playing recordings...')
        time.sleep(4)
        print('Please go to the next replica...')
        time.sleep(3)
        print('Statue # 2')
        time.sleep(1)
        print('Turning on the Lights.')
        time.sleep(1)
        print('Playing recordings...')
        time.sleep(4)
        print('Please go to the next replica...')
        time.sleep(3)
        print('Statue # 3')
        time.sleep(1)
        print('Turning on the Lights.')
        time.sleep(1)
        print('Playing recordings...')
        time.sleep(4)
        print('Please go to the next replica...')        
    elif (data['Trigger']==0):
        print("Waiting for trigger")

subscribe.callback(on_message_print, "tb/mqtt-integration/sensors", hostname="broker.hivemq.com", port=1883)