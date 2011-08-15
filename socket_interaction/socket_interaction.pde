/**
  Socket Interaction
  Author:   Andrew Fisher
  Date:     15 Aug 2011
  Technically can take any inbound serial connection but in this
  instance takes data from a web socket which has been passed
  across a serial connection from the webserver to the arduino
  Takes three variables - X, Y, Z representing the sensor array
  
  Package is made up of 6 bytes as:
  0  255  header byte
  1  255  header byte
  2  int  0-180 val for x
  3  int  0-180 val for y
  4  int  high byte for z
  5  int  low byte for z

**/

#define PACKAGE_LENGTH 6

#define RED_PIN 3
#define GREEN_PIN 5
#define BLUE_PIN 6

byte buffer_array[4];
boolean output = false;

int x, y, z = 0;

void setup() {
  Serial.begin(115200);
  Serial.println("Welcome to the view"); 
  
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
            packet_complete = true;
        } else {
            // we have half a header
            found_null = true;
        }
      }
    }
  }
            
/**      
      Serial.println(val, DEC);
      //Serial.println(val);
      if (val == 255) {
        if (found_null) {
            // we've got a message 
            //Serial.println("We have a message");
            started = true;
            found_null = false;
        } else {
            found_null = true;
        }
      } else {
        if (started) {
            // we're now processing the buffer.
            //Serial.println("message is read");
            buffer_array[0] = Serial.read();
            buffer_array[1] = Serial.read();
            buffer_array[2] = Serial.read();
            buffer_array[3] = Serial.read();
            packet_complete = true;
        } else {
            found_null = false;
            started = false;
        }
      }
          
    } **/

    // now we have some data we can do something with it.
    //Serial.println("hi");
    if (packet_complete) {
      x = buffer_array[0];
      y = buffer_array[1];
      z = (buffer_array[2]<<8) + buffer_array[3];
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
    analogWrite(GREEN_PIN, map(y, 0, 180, 0, 255));
    analogWrite(BLUE_PIN, map(z, 0, 360, 0, 255));
}
