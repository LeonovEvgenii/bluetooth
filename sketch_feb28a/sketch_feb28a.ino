#include <SoftwareSerial.h>

//SoftwareSerial mySerial(2, 3); // RX, TX
SoftwareSerial mySerial = SoftwareSerial(2,3);

void setup() {
  Serial.begin(9600);

  mySerial.begin(9600);

}

void loop() 
{
//  Serial.write("Maslov loshara");
  if (Serial.available()) 
  {
    mySerial.write(Serial.read());
  }

  if (mySerial.available()) 
  {
    Serial.write(mySerial.read());
  }

}
