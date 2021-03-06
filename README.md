
# Look at M.E.

![Project Logo](https://github.com/giovanniruocco/smartmuseum/blob/master/images/logo.png)
## IoT Course 2020 - MSc Engineering in computer science - Sapienza

We are a group of students at the MS Course in Engineering in Computer Science at the Sapienza university in Rome supported by a Design Advisor, and in this GitHub repository we will present the project that we worked on to provide the Arte Classica Museum of Sapienza a new experience for the museum visitors as well as helping the curators understand what are the most loved art pieces in the gallery.
The project was developed as part of the Internet of Things course, here are our LinkedIn profiles:

- [Ruocco Giovanni](https://www.linkedin.com/in/giovanniruocco07)
- [Ferrara Andrea Gaetano](https://www.linkedin.com/in/andrea-gaetano-ferrara-98a5371a3)
- [Vona Andrea](https://www.linkedin.com/in/andrea-vona-96b832165)
- [Gironi Camilla](https://www.linkedin.com/in/camilla-gironi)

## Repository

```
│
├── Code                  #Code for all the software parts of the project
│   │
│   ├── Arduino           #Code for the arduino sketch to flash in the board
│   │   |   
│   |   ├── sketch_may11a
│   │   |     |
│   |   |     └── sketch_may11a.ino
|   |   └── LookAtM.E._Terminal.stc
|   |
|   |
│   ├── Devices           #Code for the real and simulated devices
│   |     │
│   |     ├── realDevice1.py
│   |     ├── simulatedDevice2.py
│   |     ├── simulatedDevice3.py
│   |     ├── simulatedDevice4.py
|   |     └── simulatedDevice5.py
|   |
|   |
│   ├── WebApp           #Code for the web application
│   |     │
│   |     ├── web
│   │     |     |
│   |     |     ├── css1.css
│   |     |     ├── logo.png
│   |     |     └── museo.jpg
│   |     ├── index.html
│   |     ├── history.html
│   |     ├── info.html
|   |     └── about.html
|   |
|   |
|   └── Simulation Clients           #Code for the simulated clients
|         |
│         ├── client.py
│         ├── client2.py
|         └── client3.py
│   
│── Documentation                 #folder for the documents about the project
│   │
│   ├── 3rd Delivery.md
│   ├── Architecture_0806.md
│   ├── Design_0806.md
│   ├── Evaluation_0806.md
│   ├── Presentation_0806.md
│   └── Old Versions
│       |
|       ├── 1st Delivery
│       |      ├── 1st Delivery.md
│       |      ├── Architecture.md
│       |      ├── Design.md
│       |      ├── Evaluation.md
│       |      ├── IoT Presentation.pptx
│       |      └── Presentation.pdf
|       └── 2nd Delivery
│              ├── 2nd Delivery.md
│              ├── Architecture_2805.md
│              ├── Design_2805.md
│              ├── Evaluation_2805.md
│              └── Presentation_2805.pptx
│
│   
├── Images                         #Folder containing all the images
│   │   
|   └── ...
│      
└── ReadMe.md

```

## Description

Look at M.E. is an IoT device which is able to improve the user experience for the museum visitors and to provide important data to the museum curator.

Look at M.E. use a HC-SR04 proximity sensor implemented in a Elegoo UNO R3 board capable of activating a light-guided tour supported also by an audio explaination of the art pieces in order to emphasize differents feature of an art display.
Moreover, it can build a table to show in real time the distance to the statues of the museum visitors, to make sure that no one is getting too close to an art piece.
The project's development will be reported following each step and new implementation, in fact in this repository you can find the documents of the present state of the product as well as the older markdown files and video.

## Contents:

### Documents:

#### 08/06/2020 Updated Documents

- [Third Delivery](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/3rd%20Delivery.md)
- [Design](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/Design_0806.md)
- [Architecture](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/Architecture_0806.md)
- [Evaluation](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/Evaluation_0806.md)
- [Presentation](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/Presentation_0806.pdf)

### Video:

#### 08/06/2020 Updated Videos and Presentations

- [Look at M.E. Working Demo](https://www.youtube.com/watch?v=SqvsZhYC5cQ&feature=emb_title)

#### LinkedIn Post
- [LinkedIn Post](https://www.linkedin.com/pulse/look-me-project-built-iot-course-2020-msc-engineering-giovanni-ruocco/?trackingId=UZN6TBWQTY61JeVLmN83wg%3D%3D)


## Older Entries:

### 1st Delivery

Here you will find the documents of the project in its first presentation made in date 30/04/2020.
From the 1st delivery a lot of changes were made regarding the Design and Architecture of the project, so be sure to stay up to date!

### Documents:

#### 30/04/2020 Documents

- [Design](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/Old%20Versions/1st%20Delivery/Design.md)
- [Architecture](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/Old%20Versions/1st%20Delivery/Architecture.md)
- [Evaluation](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/Old%20Versions/1st%20Delivery/Evaluation.md)
- [Presentation](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/Old%20Versions/1st%20Delivery/Presentation.pdf)
- [1st Delivery Markdown](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/Old%20Versions/1st%20Delivery/1st%20Delivery.md)

### Video:

#### 30/04/2020 Videos and Presentations

- [Idea and Evaluation presentation](https://www.youtube.com/watch?v=_c1rHA_vbpU)
- [Technical presentation](https://www.youtube.com/watch?v=XWXVBEEmsI0&feature=youtu.be)

### 2nd Delivery

Here you will find the documents of the project state as of 28/05/2020.
Since the second delivery we have made some changes in the goal of the project so all the documents were modified accordingly.

#### 28/05/2020 Documents

- [Second Delivery](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/Old%20Versions/2nd%20Delivery/2nd%20Delivery.md)
- [Design](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/Old%20Versions/2nd%20Delivery/Design_2805.md)
- [Architecture](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/Old%20Versions/2nd%20Delivery/Architecture_2805.md)
- [Evaluation](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/Old%20Versions/2nd%20Delivery/Evaluation_2805.md)
- [Presentation](https://github.com/giovanniruocco/smartmuseum/blob/master/Documentation/Old%20Versions/2nd%20Delivery/Presentation_2805.pptx)

### Video:

#### 28/05/2020 Videos and Presentations

- [Future Plans](https://youtu.be/mgdUje6jdrk)
- [Evaluation](https://youtu.be/G556htPPm2g)
- [Technical presentation and Demo](https://www.youtube.com/watch?v=qv295bPE5Qw)
