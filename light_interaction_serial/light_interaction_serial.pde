/**
  Socket Interaction
  Author:   Andrew Fisher
  Date:     15 Aug 2011
  Technically can take any inbound serial connection but in this
  instance takes data from a web socket which has been passed
  across a serial connection from the webserver to the arduino
  Takes three variables - X, Y, Z representing the sensor array
  
  Package is made up of 7 bytes as:
  0  255  header byte
  1  255  header byte
  2  int  0-180 val for x
  3  int  high byte for y
  4  int  low byte for y
  5  int  high byte for z
  6  int  low byte for z
  
  Circuit setup:
  
  In this case we are using an RGB LED with a common anode, the individual
  colours are wired per the constants defined below and is a pretty simple
  circuit to prove the concept.
  

**/

#define PACKAGE_LENGTH 7

#define RED_PIN 3
#define GREEN_PIN 5
#define BLUE_PIN 6

byte buffer_array[4];
boolean output = false;

int x, y, z = 0;

void setup() {
  Serial.begin(115200);
  Serial.println("Welcome to the light interaction"); 
  
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
  digitalWrite(RED_PIN, HIGH);
  digitalWrite(GREEN_PIN, HIGH);
  digitalWrite(BLUE_PIN, HIGH);
}


void loop() {
  boolean packet_complete = false;
  boolean found_null = false;
  boolean started = false;

  if (Serial.available() > PACKAGE_LENGTH) { // 
    while (!packet_complete) {
      // iterate until we find a double \255 char then we can start filling the buffer
      byte val = Serial.read();
      if (val != 255) {
        // keep iterating until we get one.
        found_null = false;
      } else {
        // check to see if we've already had one/
        if (found_null) {
            // we have a header so let's get the rest of the buffer
            buffer_array[0] = Serial.read();
            buffer_array[1] = Serial.read();
            buffer_array[2] = Serial.read();
            buffer_array[3] = Serial.read();
            buffer_array[4] = Serial.read();
            packet_complete = true;
        } else {
            // we have half a header
            found_null = true;
        }
      }
    }
  }
            

    // now we have some data we can do something with it.
    if (packet_complete) {
      x = buffer_array[0];
      y = (buffer_array[1]<<8) + buffer_array[2];
      z = (buffer_array[3]<<8) + buffer_array[4];
      Serial.print("X: ");
      Serial.print(x);
      Serial.print(" Y: ");
      Serial.print(y);
      Serial.print(" Z: ");
      Serial.println(z);
      packet_complete = false;
    }
    
    // now we output to the LED
    analogWrite(RED_PIN, map(x, 0, 180, 0, 255));
    analogWrite(GREEN_PIN, map(y, 0, 360, 0, 255));
    analogWrite(BLUE_PIN, map(z, 0, 360, 0, 255));
}
