/*
   One green LED (on pin 10) lit for 3 seconds (the first LED to light up).
   Then one orange LED (on pin 11) lit for 1 second.
   Then finally one red LED (on pin 12) lit for 3 seconds.
   Two-colour light (pedestrian)

   The pedestrian light is constantly red (red LED on pin 9) and
   only turns green (LED on pin 8) once the button (on pin 2) is pressed.
   On button press
   If the button is pressed during the instant when the car traffic light is
   changing from green to orange:

   The car traffic light shows orange for 1 second
   Then the car traffic light turns red and the pedestrian light turns
   from red to green - to allow pedestrians to cross the street.
   After a 5 second pause, normal operation resumes.
   (Return immediately to the start of the 'normal operation' procedure.)
   (If the button is pressed at any other time, nothing happens.
   We agree that this may not be the most realistic situation,
   but we are keeping it simple for this assignment!)
 */
#include <Arduino.h>

void setup()
{
        pinMode(10, OUTPUT); //set green road led
        pinMode(11, OUTPUT); //set yellow road led
        pinMode(12, OUTPUT); //set red read led
        pinMode(9, OUTPUT); //set red pedestrian led
        pinMode(8, OUTPUT); //set green pedestrian led
        pinMode(2, INPUT); //set button
}

void loop()
{
        digitalWrite(9, HIGH); //light up red pedestrian led
        digitalWrite(10, HIGH); //light up green road led
        delay(3000); // Wait for 3000 millisecond(s)
        digitalWrite(10, LOW); //light down green road led

        if (digitalRead(2) == HIGH) //if button is pressed
        {
                digitalWrite(11, HIGH); //light up yellow road led
                delay(1000); // Wait for 1000 milliseconds
                digitalWrite(11, LOW); //light down yellow road led
                digitalWrite(12, HIGH); //light up red road led
                digitalWrite(9, LOW); //light down red pedestrian led
                digitalWrite(8, HIGH); //light up green pedestrian led
                delay(5000); // Wait for 5000 milliseconds
                digitalWrite(12, LOW); //light down red road led
                digitalWrite(8, LOW); //light down green pedestrian led
                digitalWrite(9, HIGH); //light up red pedestrian led
        }
        else
        {
                digitalWrite(11, HIGH); //light up yellow road led
                delay(1000); // Wait for 1000 milliseconds
                digitalWrite(11, LOW); //light down yellow road led
                digitalWrite(12, HIGH); //light up red road led
                delay(3000); // Wait for 3000 milliseconds
                digitalWrite(12, LOW); //light down red road led
        }
}
