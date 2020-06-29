/*
 * Posted on https://randomnerdtutorials.com
 * created by http://playground.arduino.cc/Code/NewPing
*/

#include <NewPing.h>


#define TRIGGER_PIN 10
#define ECHO_PIN 11
#define MAX_DISTANCE 390

const int buttonPin = 2; 
const int ledPin =  12;


int buttonState = 0;  
// NewPing setup of pins and maximum distance
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); 
int cont=0;
int pop=0;
void setup() {
   Serial.begin(9600);
     pinMode(4, OUTPUT);
   pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);

}
 
void loop() {

   delay(1000);
   unsigned int distance = sonar.ping_cm();

  buttonState = digitalRead(buttonPin);


  
 
    Serial.print("\"Trigger\":");
    if (buttonState == HIGH) {
    // turn LED on:
    digitalWrite(ledPin, HIGH);
    Serial.print(true);
  } else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
    Serial.print(false);
  }
   if (distance != 0)
  {
      Serial.print(", \"Distance\": ");
      Serial.print(distance);
  }
         Serial.println();
  if (distance <10 && distance != 0)
  {
     tone(4,100,100);
  }
  
}
