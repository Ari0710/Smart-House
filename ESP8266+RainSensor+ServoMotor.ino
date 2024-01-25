#include <Servo.h>

// Pin configuration
const int rainSensorPin = D2;  // Replace D2 with the actual pin connected to the rain sensor
const int servoMotorPin = D8;  // Replace D1 with the actual pin connected to the servo motor

Servo myServo;

void setup() {
  Serial.begin(115200);
  pinMode(rainSensorPin, INPUT);
  pinMode(servoMotorPin, OUTPUT);
  
  myServo.attach(servoMotorPin);
}

void loop() {
  // Read the rain sensor value (HIGH when rain is detected)
  int rainSensorValue = digitalRead(rainSensorPin);

  if (rainSensorValue == HIGH) {
    Serial.println("Rain detected! Rotating servo motor...");
    rotateServo(); // Add a delay to avoid continuous rotation due to noise
  } else {
    Serial.println("No rain detected.");
    myServo.write(0);

  }
}

void rotateServo() {
  myServo.write(180);  // Return the servo motor to the initial position
}