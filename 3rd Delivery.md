# Third Delivery
## Comment Received and Changes
The comment we received was about not being able of providing a meaningful indicator of a statue's popularity through a single or multiple proximity sensors. 
We realized that no matter how many proximity sensors, the data provided will never be precise enough to indicate the actual popularity of the art piece. Also, this was rather a minor issue that we intended to address, than the main goal in our project. Furthermore, the problem of estimating the popularity of an art piece was itself very popular along the other projects.
For all these reasons, we decided to abandon this point in favor a new issue, which can be at least resolved with sufficient accuracy. That is the security of the art pieces. The proximity sensors will be indeed deployed in order to establish if some visitors are getting too close to the replicas. 
In the design document we are going to represent this functionality, in the architecture we will depict how it works and finally in the evaluation we are going to examine its proper working.
## Technical Work Done From 2nd Delivery
We created a rule chain that checks whether the alarm was turned on and sends an alert via telegram bot to the security staff of the museum. Also, we added a buzzer to the board in order to beep whenever a user is getting too close to the replica.
We finished the website that will display the data collected by Thingsboard (the alarm field will be sent by Thingsboard, it won't be calculated from the website).
We created an improved version of the python scripts, in order to simulate the behavior of the illumination and the speaker for each replica. They can talk between each other through MQTT.
## Evaluation
Since we added a telegram bot there will be a problem if telegram goes down maybe for server down or unreachable because of a network problem, outage or a website maintenance in progress.

## Missing Features
Unfortunately, we were not able to replace the python scripts with real hardware due to not having it.
