#include <Servo.h>  //connect servo lib
Servo myservo; //set setvo object
int pos = 0; //start position

void setup()
{
        Serial.begin(9600); //printing
        pinMode(3, OUTPUT); // red led
        pinMode(4, OUTPUT); //green led
        pinMode(2, INPUT); //set button
        myservo.attach(9); // attach the object myservo to the servo on pin 9
}

void loop()
{
        digitalWrite(9, LOW); //do not rotate servo
        digitalWrite(3, HIGH); //turn on red LED
        if (digitalRead(2) == HIGH) //if button is pressed
        {
                Serial.println("Button pressed");
                for(pos = 0; pos < 90; pos += 1) // go from 0° to 90
                {
                        myservo.write(pos); // one step at a time
                        delay(15); // go to the position stored in 'pos'
                }
                digitalWrite(3, LOW); //turn off red LED
                digitalWrite(4, HIGH); //turn on gren LED
                delay(5000); // Wait for 5000 millisecond(s)
                digitalWrite(4, LOW); //turn off green LED
                digitalWrite(3, HIGH); //turn on red LED
                for(pos = 90; pos>=1; pos-=1) /// go from 90° to 0°
                {
                        myservo.write(pos); // go to the position stored in 'pos'
                        delay(15); // wait 15ms for the servo to move to position
                }
        }
}
