// Set up constants:
const int analogInPin = A0;   // Number of the pin connected to the potentiometer
const int analogOutPin = 8;   // Number of the pin connected to the piezo

int sensorValue = 0;          // Value read by the potentiometer
int outputValue = 0;          // Value sent to the piezo

void setup() {
        // Initialise communication with the computer
        Serial.begin(9600);

        // Indicate that the pin analogOutPin is an output:
        pinMode(analogOutPin, OUTPUT);
        // Indicate that analogInPin is an input:
        pinMode(analogInPin, INPUT);
}

void loop() {
        // Read the value of the potentiometer and
        // store that value in sensorValue:
        sensorValue = analogRead(analogInPin);
        // scale sensorValue to a value between 1 and 400
        // and store the value in outputValue:
        outputValue = map(sensorValue, 0, 1023, 1, 400);
        // send this new outputValue to the piezo
        tone(8, 50*outputValue);

        // sending the information to the computer
        Serial.print("sensor = " );
        Serial.print(sensorValue);
        Serial.print("\t output = ");
        Serial.print(outputValue);
        Serial.print("\t Hz = ");
        Serial.println(50*outputValue);
}
