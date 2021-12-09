/*
  Arduino Nano 33 BLE Getting Started
  BLE peripheral with a simple Hello World greeting service that can be viewed
  on a mobile phone
  Adapted from Arduino BatteryMonitor example
*/

#include <ArduinoBLE.h>

static const char* greeting = "Hello World!";

BLEService greetingService("180C");  // User defined service

BLEStringCharacteristic greetingCharacteristic("2A56",  // standard 16-bit characteristic UUID
    BLERead, 13); // remote clients will only be able to read this

BLEShortCharacteristic classifierCharacteristic("2A57", BLERead | BLENotify);

void setup() {
  Serial.begin(9600);    // initialize serial communication
  while (!Serial);

  pinMode(LED_BUILTIN, OUTPUT); // initialize the built-in LED pin

  if (!BLE.begin()) {   // initialize BLE
    Serial.println("starting BLE failed!");
    while (1);
  }

  BLE.setLocalName("Nano33BLE_ECE202");  // Set name for connection
  BLE.setAdvertisedService(greetingService); // Advertise service
  greetingService.addCharacteristic(greetingCharacteristic); // Add characteristic to service
  greetingService.addCharacteristic(classifierCharacteristic); // Add characteristic to service
  BLE.addService(greetingService); // Add service
  greetingCharacteristic.setValue(greeting); // Set greeting string
  classifierCharacteristic.setValue(123); // Set greeting string

  BLE.advertise();  // Start advertising
  Serial.print("Peripheral device MAC: ");
  Serial.println(BLE.address());
  Serial.println("Waiting for connections...");
}

void loop() {
  BLEDevice central = BLE.central();  // Wait for a BLE central to connect

  // if a central is connected to the peripheral:
  if (central) {
    Serial.print("Connected to central MAC: ");
    // print the central's BT address:
    Serial.println(central.address());
    // turn on the LED to indicate the connection:
    digitalWrite(LED_BUILTIN, HIGH);
    unsigned int current_time = millis();
    while (central.connected()){
        if (millis() > current_time+5000){ //can't immediately start doing things while pairing occurs
          Serial.print("Simulating blender: ");
          for (int i = 0; i<8; i++) { //pretend blender is on for 8 seconds, should cause a notification.
            delay(1000);
            classifierCharacteristic.setValue(0);//number for blender
          }
          
          delay(5000); //wait 30 seconds before the other type of testing
          
          //pretend fridge was open for 7 seconds, should cause a notification.
          Serial.print("Simulating fridge: ");
          classifierCharacteristic.setValue(4);//number for fridge
          delay(7000);
          classifierCharacteristic.setValue(4);//number for fridge
        }
      } // keep looping while connected
    
    // when the central disconnects, turn off the LED:
    digitalWrite(LED_BUILTIN, LOW);
    Serial.print("Disconnected from central MAC: ");
    Serial.println(central.address());
  }
}
