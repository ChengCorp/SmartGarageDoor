//OVERVIEW
///////////////////////////////////////////////////////////////////////////////////////////
// This script reads and converts the states of the hall effect sensors into garage door
// open/close states and then output the data to serial.

// Since it takes a couple seconds for the garage door to open, it may be best to track a
// third state called "opening/closing". 
///////////////////////////////////////////////////////////////////////////////////////////

//SENSORS
///////////////////////////////////////////////////////////////////////////////////////////
// The hall effect sensor (US1881) used in this project is a latched sensor, which means
// once the sensor is toggled by a magnet, it will maintain its state until an opposite
// pole is used to unlatch it.

// Since what I want is a reed switch, I need to cycle the power pin on (for 10+ ms) and
// off (for 10+ ms) to reset the sensor to unlatched state after latching.
//////////////////////////////////////////////////////////////////////////////////////////


boolean bypass = true;

int open_pin = 2;
int close_pin = 3;

int power_pin = 12;

int output_pin = 13; // for arduino led display

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  
  // make the open_pin an input:
  pinMode(open_pin, INPUT);
  pinMode(close_pin, INPUT);
  
  // make the power_pin an output to apply alternate power.
  pinMode(power_pin, OUTPUT);
  
  pinMode(output_pin, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {

  // apply power for 50 ms
  digitalWrite(power_pin, HIGH);
  delay(50);
  
  // read the input pin:
  int openState = digitalRead(open_pin);
  int closeState = digitalRead(close_pin);
  
  if (bypass) {
    closeState = !openState;
  }
  
  // print out the state of the door:
  if (!openState && closeState) { // close
    Serial.println(0);
    digitalWrite(output_pin, LOW);
  } else if (openState && !closeState) { // open
    digitalWrite(output_pin, HIGH);
    Serial.println(1);
  } else if (!openState && !closeState) { // opening/closing
    Serial.println(2);
  } else {
    Serial.println(3); // error
  }
  
  // turn off power for reset.
  digitalWrite(power_pin, LOW);
  delay(50);
}



