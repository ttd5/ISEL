// Define Macros
#define PINLED1 10
#define PINLED2 11
#define PINBTN 8
#define PINPOT A0
#define PINUP A1
#define PINLDR A2
// Global Variables
unsigned int aR;
float luminosidade;
int count = 0;
// Global functions

// 2(a1) Function that reads the signal and returns the tension 
float voltage(byte pin) {
  aR = analogRead(pin);
  return (aR * 5.0) / 1023.0;
}

// 2(a2) Function that returns the position of a given tension ...
float pos(byte pin) {
  return (voltage(pin) * 360.0) / 5.0;
}
// 2(a2) ... and the brightness
float bright(byte pin) {
  float ldrRes = 10 * ((5.0/voltage(pin)) - 1);
  return (43.141 * pow(ldrRes, -(1/0.837)));
}

void pressed() {
    int isPressed = digitalRead(PINBTN);
    if(isPressed == 0) {
      Serial.print("1\t");
    }
    else {
      Serial.print("0\t");
    }
}

// 2(b) Prints the values to the console
void prints(byte pin) {
  Serial.print((String)millis() + '\t'); // timestamp in milliseconds (ms)
  Serial.print((String)voltage(pin) + '\t'); // Voltage (v) 
  Serial.print((String)pos(pin) + '\t'); // Position (x)
  pressed(); // pressed (0/1)
  Serial.println((String)bright(pin)); // Brightness (%)
  delay(1000);
}

// 2(c) Read, Write and print only twice per second
void twice(byte pin) {
  for (int i = 0; i < 2; i++) { 
      prints(pin);
  }
  delay(500);
}

// 3(a) Frequency value controls by a given tension D1 brightness
void controlLedByFrequency(float v) {
  float half_T = (500.0/0.5 - 500.0/50.0)/(-5.0) * v + 500/0.5;
  digitalWrite(PINLED1, HIGH);
  delay(half_T);
  digitalWrite(PINLED1, LOW);
  delay(half_T);
}

// 3(b) test LED2 for it's brightness between 0 and 255, (0% - 100%)
void controlLedByPercentage(int percentage) {
  float brightness = (percentage * 100.0) / 255.0;
  analogWrite(PINLED2, brightness);
}

// 4(a) Pot regulates the value of led D1
void controlLedByPot() {
  digitalWrite(PINLED1, HIGH);
  delay(voltage(PINPOT));
  digitalWrite(PINLED1, LOW);
  delay(voltage(PINPOT));
}

// 4(b) Values from the console controls D2
void controlLedByConsole() {
  if(Serial.available()) {
    int input = Serial.parseInt();
    luminosidade = input * 2.55;
  }
  analogWrite(PINLED2, luminosidade);
}

// 4(c) Increments by pressing a button
int incrementPressed() {
  int btnState = digitalRead(PINBTN);
  if (btnState == 1) {
    count++;
  }
  delay(1000);
  return count;
}

void setup() {
  // Baud
  Serial.begin(9600);
  // Configure pins
  pinMode(PINLED1, OUTPUT);
  pinMode(PINLED2, OUTPUT);
  pinMode(PINLDR, INPUT);
  pinMode(PINBTN, INPUT);
  pinMode(PINUP, INPUT);
}

void loop() {
  // S1 Potenciometro
  // prints(PINPOT);
  // S2 botao com pullup
  // prints(PINUP);
  // S3 botao
  // prints(PINBTN);
  // S4 LDR com pullup
  prints(PINUP);
  // 2(c) prints twice
  // twice(PINBTN);
  // 3(a) LED1 by frequency
  // controlLedByFrequency(3); 
  // 3(b) LED2 by percentage
  // controlLedByPercentage(50);
  // S5 4(a) LED1
  // controlLedByPot();
  // S6 4(b) LED2
  // controlLedByConsole();
  // 4(c)
  // Serial.println(incrementPressed());
}
