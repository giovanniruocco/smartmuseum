#  *Architecture*

###  **Look at M.E.**


In this document we will review the new state of the architecture of Look at M.E. with all the changes taken to address the main problems and details pointed out in the first presentation of the project.

The older version of this document will be available in the main repository of Look at M.E. so that anyone who wishes to can take a look at the evolution of the project.

[Older Architecture version](https://github.com/giovanniruocco/smartmuseum/blob/master/Architecture.md)

Look at M.E. is built in a Elegoo UNO R3 board in which we implemented an HC-SR04 ultrasonic proximity sensor to determine whether a visitor is in the “attention area” for each statue. Also we will use a button to trigger the changing of the lighting and sound of the room to create for the user a guided tour in the room.

As for the software components, we created the main firmware file in the Arduino IDE, the telemetries will be managed by the cloud-based broker Thingsboard and then retrieved on a web page to show all the important information to the museum curator.

The telemetries about the popularity of the art pieces and the lighting control will be sent via MQTT to our cloud broker. The telemetries will be then retrieved by the external hardware components that subscribe to the respective topic to receive updates.

Let’s take a look at each component that makes our product starting with the hardware.

![System](https://github.com/giovanniruocco/smartmuseum/blob/master/images/system.jpg)

## **Hardware**

### **Elegoo UNO R3**


Elegoo UNO R3
The ELEGOO UNO is a microcontroller board based on the ATmega328 (datasheet). It
has 14 digital input/output pins (of which 6 can be used as PWM outputs), 6 analog
inputs, a 16 MHz crystal oscillator, a USB connection, a power jack, an ICSP header, and
a reset button. It contains everything needed to support the microcontroller; simply
connect it to a computer with a USB cable or power it with an AC-to-DC adapter or
battery to get started.

![Board](https://github.com/giovanniruocco/smartmuseum/blob/master/images/board1_28.PNG)

The entire board’s datasheet can be found at the following link:

[Datasheet](https://epow0.org/~amki/car_kit/Datasheet/ELEGOO%20UNO%20R3%20Board.pdf)

Others of its main features are:

- Microcontroller_____________________________________________________ATmega328

- Operating Voltage __________________________________________________5 V

- Input Voltage (recommended)________________________________________7-12 V

- Input Voltage (limits) ________________________________________________6-20 V

- Digital I/O Pins  _____________________________________________________14

- Analog Input Pins ___________________________________________________6

- DC Current per I/O Pin______________________________________________40 mA

- DC Current for 3.3V Pin_____________________________________________50 mA

- Flash Memory ______________________________________________________32 KB

- SRAM ______________________________________________________________2 KB

- EEPROM ___________________________________________________________1 KB

- Clock Speed ________________________________________________________16 MHZ

![Board](https://github.com/giovanniruocco/smartmuseum/blob/master/images/board2_28.PNG)

![Scheme](https://github.com/giovanniruocco/smartmuseum/blob/master/images/boardScheme.PNG)
	
---

### **The HC-SR04 proximity sensor**

The HC­SR04 ultrasonic sensor uses sonar to determine distance to an object like bats or dolphins do. It offers excellent non­contact range detection with high accuracy and stable readings in an easy­to­use package. It operates in a distance range going from 2cm to 400 cm. Its operation is not affected by sunlight or black material like Sharp rangefinders are (although acoustically soft materials like cloth can be difficult to detect). It comes complete with an ultrasonic transmitter and receiver module.
![Sensor 1](https://github.com/giovanniruocco/smartmuseum/blob/master/images/sensor1.PNG)

The main features are :

Features:

 - Power Supply :+5V DC
   
  -  Quiescent Current : <2mA
   
   - Working Current: 15mA
   
   - Effectual Angle: <15°
   
   - Ranging Distance : 2cm – 400 cm
   
   - Resolution : 0.3 cm
   
   - Measuring Angle: 30 degree
   
   - Trigger Input Pulse width: 10uS
   
   - Dimension: 45mm x 20mm x 15mm

![Sensor 2](https://github.com/giovanniruocco/smartmuseum/blob/master/images/sensor2.PNG)

The sensor come with 4 pins that correspond to :

VCC = +5VDC

Trig = Trigger input of Sensor

Echo = Echo output of Sensor

GND = GND

To start the measurement, Trig of SR04 must receive a pulse of high (5V) for at least 10us, this will initiate the sensor will transmit out 8 cycle of ultrasonic burst at 40kHz and wait for the reflected ultrasonic burst. When the sensor detected ultrasonic from the receiver, it will set the Echo pin to high (5V) and delay for a period (width) which proportion to distance. To obtain the distance, measure the width (Ton) of the Echo pin.

----
### **Other Hardware Components**

In the actual production of the project we needed and implemented other hardware components; these are just standard components needed to complete the product but have no specific purpose.

- 1 Breadboard

- 1 coloured LED

- 1 button

- 2 resistors


---

### **External Hardware**

Also, we have some hardware external to our board, for example the light and sound system that our application will use to express its full potential. In fact this will subscribe to the topic in our broker so that on a new trigger message the guided tour will start. These are external since we are not implementing them on the board but must be connected to our broker in order to receive the values that trigger them, but we will simulate them via simple clients script that retrieve values via MQTT.


# **Software and tools**

The software components and tools of the product are a lot and different in their purposes; we have in fact different software to create the firmware and show collected data that uses libraries and APIs to access the sensor or publish telemetries.


### **Arduino IDE**


The Arduino Integrated Development Environment - or Arduino Software (IDE) - contains a text editor for writing code, a message area, a text console, a toolbar with buttons for common functions and a series of menus. It connects to the Arduino and Genuino hardware to upload programs and communicate with them.

Programs written using Arduino Software (IDE) are called sketches. These sketches are written in the text editor and are saved with the file extension .ino. The editor has features for cutting/pasting and for searching/replacing text. The message area gives feedback while saving and exporting and also displays errors. The console displays text output by the Arduino Software (IDE), including complete error messages and other information. The bottom righthand corner of the window displays the configured board and serial port. The toolbar buttons allow you to verify and upload programs, create, open, and save sketches, and open the serial monitor.

---

### **MQTT**


MQTT stands for MQ Telemetry Transport. It is a publish/subscribe, extremely simple and lightweight messaging protocol, designed for constrained devices and low-bandwidth, high-latency or unreliable networks. The design principles are to minimise network bandwidth and device resource requirements whilst also attempting to ensure reliability and some degree of assurance of delivery. These principles also turn out to make the protocol ideal of the emerging “machine-to-machine” (M2M) or “Internet of Things” world of connected devices, and for mobile applications where bandwidth and battery power are at a premium.


---

### **Coolterm**


CoolTerm is a simple serial port terminal application (no terminal emulation) that is geared towards hobbyists and professionals with a need to exchange data with hardware connected to serial ports such as servo controllers, robotic kits, GPS receivers, microcontrollers, etc.
We will use it to have a better control on the terminal and to create a textfile that will be used to send the publish message to the broker.

---

### **Python Script**


Once our board is programmed and is sending data for the popularity, distance and trigger values, we create a text file that is updated every new value received.

Then, using the python script we will connect to the device in Thingsboard and will a publish of the text file that contains the data in JSON format.

---

### **Thingsboard**

ThingsBoard is an open-source IoT platform that enables rapid development, management and scaling of IoT projects. Its goal is to provide the out-of-the-box IoT cloud or on-premises solution that will enable server-side infrastructure for your IoT applications.

With ThingsBoard, you are able to:

- Provision devices, assets and customers and define relations between them.

- Collect and visualize data from devices and assets.

- Analyse incoming telemetry and trigger alarms with complex event processing.

- Control your devices using remote procedure calls (RPC).

- Build work-flows based on device life-cycle event, REST API event, RPC request, etc

- Design dynamic and responsive dashboards and present device or asset telemetry and insights to your customers

- Enable use-case specific features using customizable rule chains.

- Push device data to other systems.

This is the place where all the data we send will be stored, we can then use the received messages to trigger functions that will improve the user experience in the museum, or we can show them on a web page in a user-friendly format.

In order to use the site, we will need a free account that can be created following the standard procedure.

---

### **Web Application**

The web application will only have the purpose to show the popularity data to the museum curator so he can have a view on the most appreciated statues and act accordingly.

It will be a simple HTML page with some CSS style and some Javascript code that will manage the REST API from thingsboard to collect data from the Thingsboard database.

The web page will be accessible only by authorized staff so that the info stored in it can be kept safe.

![Web App Mockup](https://github.com/giovanniruocco/smartmuseum/blob/master/images/mockup.jpg)


