// TESTE 2
//EXERCICIO 1
/**
#define R2 7
#define BUTTON 3
#define LDR A2
#define LED 6

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

float brilhoLDR(int pin) {
  float R1 = R2 * (1023/analogRead(pin) - 1);
  return pow(R1/100,-1/0.7);
}

void brilhoLED(int pin, float perCent) {
  analogWrite(LED, perCent * 255 / 100);
}

void consolaCSV() {
  Serial.print(bLED, 3);
  Serial.print('\t');
  Serial.print(bLDR, 3);
  Serial.print('\n');
}

void loop() {
  int bLED = brilhoLDR(LDR) ;
  int bLDR = map(bLDR, 0 , 100, 100, 0);
  brilhoLED(LED,bLED);
  consolaCSV();
  if (digitalRead(BOTAO) == 0) {
    for (int x = 0; x <=24; x++) {
      brilhoSimulado(x*3600);
      delay(1000);
  }
}
}
float brilhoSimulador(unsigned long t) {
  return 45 + 15 * sin(6.28 * t / 1000 / (3600 * 24));
}
//EXERCICIO 2
#define POTE A0
#define PIEZO 3
#define LA4 440
#define LA5 880
#define LA6 1760
#define LA7 3520

void setup() {
  pinMode(PIEZO, OUTPUT);
}

void loop(){
  unsigned int x = analogRead(POTE);
  if (x >= 0 && x < 256) {
    tone(PIEZO, LA4);
  }
  if (x >= 256 && x < 512) {
    tone(PIEZO, LA5);
  }
  if (x >= 512 && x < 768) {
    tone(PIEZO, LA6);
  }
  if (x >= 768 && x < 1024) {
    tone(PIEZO, LA7);
  }
}
*//
float fMin = 1, fMax = 80;
float f = fMin;
bool state = 0;
unsigned long t0 = millis();
void loop() {

  digitalWrite(TRIGGER, HIGH);
  delayMicrodeconds(10);
  digitalWrite(TRIGGER, LOW);
  
  float d = pulseIn(ECHO)/48.0; 
  f = map(d, 20, 200, fMin, Fmax);
  f = constrain(f, fMin, Fmax);
  
  digitalWrite(LED, HIGH);
  delay(500/f);
  digitalWrite(LED, LOW);
  delay(500/f);
}