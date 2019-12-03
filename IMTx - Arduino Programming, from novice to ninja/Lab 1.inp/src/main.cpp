/*
   This task builds on the functions you saw in Blink and the electronics you
   have learned about this week, you must create a traffic light with three LEDs
   (one green on pin 4, one amber on pin 3, and one red on pin 2)
   which must light up in the following sequence:

   Green, lit for 3 seconds (the green LED must be the first one to light up)
   Amber, lit for 1 seconds (and the green light must turn off when the amber light turns on)
   Then finally the red light should be on by itself for 3 seconds
   This sequence must be executed over and over while the Arduino is powered on.
 */
#include <Arduino.h>

void setup()
{
        pinMode(2, OUTPUT);
        pinMode(3, OUTPUT);
        pinMode(4, OUTPUT);
}

void loop()
{
        digitalWrite(4, HIGH);
        delay(3000); // Wait for 1000 millisecond(s)
        digitalWrite(4, LOW);
        digitalWrite(3, HIGH);
        delay(1000); // Wait for 1000 millisecond(s)
        digitalWrite(3, LOW);
        digitalWrite(2, HIGH);
        delay(3000); // Wait for 1000 millisecond(s)
        digitalWrite(2, LOW);
}
