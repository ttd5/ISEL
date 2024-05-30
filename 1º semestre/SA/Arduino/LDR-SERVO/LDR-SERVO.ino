#define LED 3
#define LDR A0
#include <Servo.h>
Servo servo;

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(LDR, INPUT);
  servo.attach(5);
}

void loop() {
  if (analogRead(LDR)) {
    int brilho = map(analogRead(LDR), 0, 1023, 0, 180);
    Serial.println(brilho);
    analogWrite(LED,brilho);
    servo.write(brilho);
    delay(100);
  }
}
