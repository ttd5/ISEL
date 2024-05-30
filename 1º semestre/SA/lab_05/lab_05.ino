
// Circuito 5: Onda sinusoidal
#include <Servo.h>
#define PINSERVO 10

Servo servo;
int pos = 0;
  
void setup() {
	servo.attach(10);
  	Serial.begin(9600);
}

void loop() {
  for(pos = 0;pos <= 180; pos += 5) {
  	servo.write(pos);
    float wave = 90 * sin((PI/5.0) * pos);
    Serial.print(wave);
  }
  for(pos = 180;pos >= 0; pos -= 5) {
  	servo.write(pos);
    float wave = 90 * sin((PI/5.0) * pos);
    Serial.print(wave);
  }
}


// Circuito 4: LEDRGB - Serial
#define PINLEDBLUE 9
#define PINLEDGREEN 10
#define PINLEDRED 11
#define BAUD_RATE 9600
// Global Variables
unsigned int aR;
int i = 0;

int ri = 0;
int gi = 0;
int bi = 1;
int red = 0;
int green = 0;
int blue = 0;

void setup() {
  // Pin Config
  pinMode(PINLEDRED, OUTPUT);
  pinMode(PINLEDGREEN, OUTPUT);
  pinMode(PINLEDBLUE, OUTPUT);
  Serial.begin(BAUD_RATE);
  newRGB();

}
void rgbColor(float red, float green, float blue) {
  analogWrite(PINLEDBLUE, blue * 2.55);
	analogWrite(PINLEDRED, red * 2.55);
  analogWrite(PINLEDGREEN, green * 2.55);
}  

void newRGB() {
  int green = 255;
  int blue = 255;
  int red = 0;
  for (green = 255; green > 0; green -= 5) {
    analogWrite(PINLEDGREEN, green);
    delay(50);
  } 
  for(red = 0; red < 255; red+=5) {
      analogWrite(PINLEDRED, red);
      delay(50);  
  }
  for(blue = 255; blue > 0; blue -= 5) {
      analogWrite(PINLEDBLUE, blue);
      delay(50);  
  }
  for(red = 255; red > 0; red -= 5) {
      analogWrite(PINLEDRED, red);
      delay(50);  
  } 
  for(green = 0; green < 255; green+=5) {
      analogWrite(PINLEDGREEN, green);
      delay(50);  
  }
  for(blue = 0; blue < 255; blue+=5) {
      analogWrite(PINLEDBLUE, blue);
      delay(50);  
  }
}
void loop() {
  // Normal way
  /*if(Serial.available()) {
    float red = 0, green = 0, blue = 0;
   	red = Serial.parseInt();
    green = Serial.parseInt();  
    blue = Serial.parseInt();
    rgbColor(red, green, blue);
  }*/
  /*
  // Flowing way
  red += ri;
  green += gi; 
  blue += bi;
  if(blue > 255) {
    blue = 255;
    ri = random(1, 5);
    bi = -1 * random(1, 5);
  }
  else if(blue < 0) {
    blue = 0;
    bi = 0;
  }
  if (red > 255) {
    red = 255;
    gi = random(1, 5);
    ri = -1 * random(1, 5); 
  }
  else if(red < 0) {
    red = 0;
    ri = 0;
  }
  if(green > 255) {
    green = 255;
    bi = random(1, 5);
    gi = -1 * random(1, 5);
  }
  else if(green < 0) {
    green = 0;
    gi = 0;
  }
  rgbColor(red, green, blue);
  */
  delay(50);
}


// Circuito 2: SONAR - BUZZER
#define PINBUZZ 2
#define PINTRIGGER 12
#define PINECHO 13
// Criar o pico do buzzer 
void beep() {
  digitalWrite(PINBUZZ, HIGH);
  delay(50);
  digitalWrite(PINBUZZ, LOW);
}
void setup() {
  Serial.begin(9600);
  pinMode(PINECHO, INPUT);
  pinMode(PINTRIGGER, OUTPUT);
  pinMode(PINBUZZ, OUTPUT);
}
void loop() {
  digitalWrite(PINTRIGGER, HIGH);
  delayMicroseconds(10);
  digitalWrite(PINTRIGGER, LOW);
  int duration = pulseIn(PINECHO, HIGH);
  int distance = (duration/2) / 29.1;
  // Verificar se está entre a distancia compreêndida, 5cm - 50cm
  if(distance <= 50 && distance >= 5) {
    int freq = map(distance, 5, 50, 0.5, 20);
    delay(freq); // Changes with the freq
    beep();	
    // See the current distance
    Serial.print("Distance: ");
    Serial.println(distance);
  } else {
    digitalWrite(PINBUZZ, LOW);
  }
}

/*
// Circuito 3: LDR - PIEZO
#define PINLDR A0
#define PINPIEZO 9

void setup()
{
  pinMode(PINLDR, INPUT);
  Serial.begin(9600);
  pinMode(PINPIEZO, OUTPUT);
}

void loop()
{
  int ldrValue = map(analogRead(PINLDR), 0, 1023, 0 ,100); // percent
  int freq = map(ldrValue, 0, 100, 200, 10000); // freq
  Serial.println(freq);
  tone(PINPIEZO, freq);
}
*/

// Circuito 1: Servo - Potenciometro
#include <Servo.h>
#define PINPOT A0

Servo servo;

void setup()
{
  servo.attach(3);
  Serial.begin(9600);
}

void loop()
{
  int aR = analogRead(PINPOT);
  // Rodar entre -90 e 90 graus
  int val = map(aR, 0, 1023, 0, 180);
  servo.write(val);
  delay(15);
}
