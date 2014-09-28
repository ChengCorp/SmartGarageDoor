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

// Configuration setup
#define bypass true

// Input pins
#define top_sensor_pin 2
#define bottom_sensor_pin 3

// Output pins
#define top_power_pin 11
#define bottom_power_pin 12

#define output_pin 13 // for arduino led display

#define door_switch_pin 7

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  
  // make the top_sensor_pin an input:
  pinMode(top_sensor_pin, INPUT);
  pinMode(bottom_sensor_pin, INPUT);
  
  // make the power_pin an output to apply alternate power.
  pinMode(top_power_pin, OUTPUT);
  pinMode(bottom_power_pin, OUTPUT);
  
  pinMode(output_pin, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {

  // apply power for 50 ms
  digitalWrite(top_power_pin, HIGH);
  delay(50);
  
  // read the input pin:
  int openState = digitalRead(top_sensor_pin);
  int closeState = digitalRead(bottom_sensor_pin);
  
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
  digitalWrite(top_power_pin, LOW);
  delay(50);
}

