#define pinLED 5
#define BOTAO 4
#define POTE A2
float tensao;

void setup() {
Serial.begin(9600);
pinMode(pinLED, OUTPUT);
pinMode(BOTAO, INPUT);

}

void loop() {
  digitalWrite(pinLED, HIGH);
  if(digitalRead(BOTAO)==HIGH) {

    tensao = map(analogRead(POTE), 0, 1023, 0, 5);
    Serial.println(tensao);   
  }
    if(tensao > 2.5) {
      digitalWrite(pinLED,LOW);
      delay(125);
      digitalWrite(pinLED, HIGH);
      delay(125);
      digitalWrite(pinLED,LOW);
      delay(125);
      digitalWrite(pinLED, HIGH);
      delay(125);
    
  }
}
