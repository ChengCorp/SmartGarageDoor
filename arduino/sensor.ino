// The hall effect sensor (US1881) used in this project is a latched sensor, which means
// once the sensor is toggled by a magnet, it will maintain its state until an opposite
// pole is used to unlatch it.

// Since what I want is a reed switch, I need to cycle the power pin on (for 10+ ms) and
// off (for 10+ ms) to reset the sensor to unlatched state after latching.

int open_pin = 2;

int power_pin = 13;

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  
  // make the open_pin an input:
  pinMode(open_pin, INPUT);
  
  // make the power_pin an output to apply alternate power.
  pinMode(power_pin, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {

  // apply power for 10 ms
  digitalWrite(power_pin, HIGH);
  delay(50);
  
  // read the input pin:
  int buttonState = digitalRead(open_pin);
  // print out the state of the button:
  Serial.println(buttonState);
  
  // turn off power for reset.
  digitalWrite(power_pin, LOW);
  delay(50);
}



