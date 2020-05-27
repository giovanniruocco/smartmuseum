# Second Delivery
## Comments Received
Most relevant comment:
> Nice presentation. I like the idea of the illumination even because there are specific challenges in terms of actuation. In terms of evaluation I think you could employ control groups, namely measure the difference with and without illumination. Is LORA responsive enough? You mention illumination is not controlled in your board?!?

As the commentator suggested, LORA is not responsive enough. So, in order to address this issue we have made some changes that will be explained in the next section of this document.
About the last part of the comment, there was a misunderstanding. The illumination is, indeed, controlled by the board, just not directly. It means that we intend to use MQTT lamps that will subscribe to the broker through specific topics and will respond based on the messages published by the board.

Other comments regarded what criteria we were going to follow, to order the replicas through the light-guided path. We do not intend to address this issue, because we believe that it's not our duty and neither we have the competences to. Instead we intend to support the curator of the museum through this process.

## Changes
The major change is leaving LORA in favor of a pure MQTT architecture for the communications between the end nodes and the cloud infrastructure (ThingsBoard). This had repercussions on the hardware used, in particular, we switched from a B-L072Z-LRWAN1 "st-lora" board to a ELEGOO UNO microcontroller.
The ELEGOO UNO microcontroller will use a Bluetooth module to send the data to a pc. The next section will provide more details about the new architecture.

## Technical Work Done So Far
Up to this moment, we have developed the firmware for the ELEGOO UNO microcontroller. It is fully operative in controlling the proximity sensors, the button and the led. Through a Bluetooth module it communicates with a pc that has a python script running which has two functions: storing persistently the data and publishing data to the MQTT "HiveMQ" broker. This broker will forward the messages to both the MQTT clients subscribed and the ThingsBoard broker.

## Momentarily Missing Features
The clients are python scripts which emulate the behavior of both the illumination and the smart speakers, which will be replaced with real ones. 
The web application is still working in progress.

## Current Evaluation
From a technical point of view we have begun to consider the precision of the proximity sensors, which we are using to measure the replicas' popularity. Also, we have deployed a very naive system for measuring the popularity which will be improved in the final deliver.
From a user point of view, the results of the survey are displayed in the below chart.
![Survey](https://github.com/giovanniruocco/smartmuseum/blob/master/images/Survey.PNG)
## Further Evaluations
In the final delivery of the project, we intend to collect users' reviews for the different rooms in the museum, focusing on the impact of Look at M.E. by confronting the result of the rooms with and without Look at M.E.
