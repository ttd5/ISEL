/* 
  Projeto tem de incluir os seguintes componentes
  1- Medidor de distancias(sonar) 
  -> void distance(int pinTrig, int pinEcho, int rate = 10)
  2- Impressora para consola
  -> void printCSV(int rate = 2, float val1, float val2)
  3- Recetor numeros inteiros(porta serial)
  -> void receiveInt()
  4- Tocar melodia(piezo)
  -> void melodia(int duration, int nota1, int nota2)
  5- Detetor toque(botao)
  -> void toque(int pinBotao)
  6- Contador(botao)
  -> void contador(int pin)
  7- Gerador sinais(onda sinusoidal, ou triangular, ou quadrada)
  -> void gerador(int rate, int periodo, char tipoOnda)
*/
static int val = 0; 
void receiveInt() {
  static const int WAIT = 0, READ = 1;
  static int state = WAIT;

  switch (state) {
  //ESPERAR PELO INPUT NA CONSOLA
  case WAIT:
    if(Serial.available() > 0) {
      state = READ;     
    }
  break;
  //ATRIBUIR VALOR DA CONSOLA
  case READ:
  val = Serial.parseInt();
  Serial.println("Escolheu a " + (String)val + "ª oitava.");
  state = WAIT;
  break;    
  }
}

#define PINTRIG 8
#define PINECHO 9

//PROJETO PIANO
#define BTN1 4
#define BTN2 5
#define BTN3 6
#define BTN4 9
#define BTN5 10
#define BTN6 11
#define BTN7 12
#define PIEZO 3

void toque1(int pinBotao, int nota) {
  int buttonPressed = 0;
  static const int WAIT = 0, PLAY = 1;
  static int state = WAIT;

  switch (state) {
    
    case WAIT:
    buttonPressed = digitalRead(pinBotao);
      if(buttonPressed == LOW) {
        state = PLAY;
      }
    break;

    case PLAY:
    buttonPressed = digitalRead(pinBotao);
    tone(PIEZO, nota);
    if(buttonPressed == HIGH) {
      Serial.println("Dó");
      state = WAIT;
      noTone(PIEZO);
      
    }
    break;
  }
}
void toque2(int pinBotao, int nota) {
  int buttonPressed = 0;
  static const int WAIT = 0, PLAY = 1;
  static int state = WAIT;

  switch (state) {
    
    case WAIT:
    buttonPressed = digitalRead(pinBotao);
      if(buttonPressed == LOW) {
        state = PLAY;
      }
    break;

    case PLAY:
    buttonPressed = digitalRead(pinBotao);
    tone(PIEZO, nota);
    if(buttonPressed == HIGH) {
      Serial.println("Ré");
      state = WAIT;
      noTone(PIEZO);
      
    }
    break;
  }
}
void toque3(int pinBotao, int nota) {
  int buttonPressed = 0;
  static const int WAIT = 0, PLAY = 1;
  static int state = WAIT;

  switch (state) {
    
    case WAIT:
    buttonPressed = digitalRead(pinBotao);
      if(buttonPressed == LOW) {
        state = PLAY;
      }
    break;

    case PLAY:
    buttonPressed = digitalRead(pinBotao);
    tone(PIEZO, nota);
    if(buttonPressed == HIGH) {
      Serial.println("Mi");
      state = WAIT;
      noTone(PIEZO);
    }
    break;
  }
}
void toque4(int pinBotao, int nota) {
  int buttonPressed = 0;
  static const int WAIT = 0, PLAY = 1;
  static int state = WAIT;

  switch (state) {
    
    case WAIT:
    buttonPressed = digitalRead(pinBotao);
      if(buttonPressed == LOW) {
        state = PLAY;
      }
    break;

    case PLAY:
    buttonPressed = digitalRead(pinBotao);

    tone(PIEZO, nota);
    if(buttonPressed == HIGH) {
       Serial.println("Fá");
       state = WAIT;
      noTone(PIEZO);
    }
    break;
  }
}
void toque5(int pinBotao, int nota) {
  int buttonPressed = 0;
  static const int WAIT = 0, PLAY = 1;
  static int state = WAIT;

  switch (state) {
    
    case WAIT:
    buttonPressed = digitalRead(pinBotao);
      if(buttonPressed == LOW) {
        state = PLAY;
      }
    break;

    case PLAY:
    buttonPressed = digitalRead(pinBotao);
    
    tone(PIEZO, nota);
    if(buttonPressed == HIGH) {
      Serial.println("Sol");
      state = WAIT;
      noTone(PIEZO);
    }
    break;
  }
}
void toque6(int pinBotao, int nota) {
  int buttonPressed = 0;
  static const int WAIT = 0, PLAY = 1;
  static int state = WAIT;

  switch (state) {
    
    case WAIT:
    buttonPressed = digitalRead(pinBotao);
      if(buttonPressed == LOW) {
        state = PLAY;
      }
    break;

    case PLAY:
    buttonPressed = digitalRead(pinBotao);
   
    tone(PIEZO, nota);
    if(buttonPressed == HIGH) {
       Serial.println("Lá");
       state = WAIT;
      noTone(PIEZO);
    }
    break;
  }
}
void toque7(int pinBotao, int nota) {
  int buttonPressed = 0;
  static const int WAIT = 0, PLAY = 1;
  static int state = WAIT;

  switch (state) {
    
    case WAIT:
    buttonPressed = digitalRead(pinBotao);
      if(buttonPressed == LOW) {
        state = PLAY;
      }
    break;

    case PLAY:
    buttonPressed = digitalRead(pinBotao);
    tone(PIEZO, nota);
    if(buttonPressed == HIGH) {
      Serial.println("Si");
      state = WAIT;
      noTone(PIEZO);
      
    }
    break;
  }
}

void setup() {
  //PROJETO PIANO
  Serial.begin(9600);
  pinMode(BTN1, INPUT_PULLUP);
  pinMode(BTN2, INPUT_PULLUP);
  pinMode(BTN3, INPUT_PULLUP);
  pinMode(BTN4, INPUT_PULLUP);
  pinMode(BTN5, INPUT_PULLUP);
  pinMode(BTN6, INPUT_PULLUP);
  pinMode(BTN7, INPUT_PULLUP);
  //
  pinMode(PIEZO, OUTPUT);
  pinMode(PINTRIG, OUTPUT);
  pinMode(PINECHO, INPUT);
  Serial.println("Escolha a sua oitava:");
}
void loop() {
//PROJETO PIANO
receiveInt();
 switch (val) {
  case 0:
  toque1(BTN1, 523);
  toque2(BTN2, 587);
  toque3(BTN3, 659);
  toque4(BTN4, 698);
  toque5(BTN5, 783);
  toque6(BTN6, 880);
  toque7(BTN7, 971);
  break;  
  case 1:
  toque1(BTN1, 32);
  toque2(BTN2, 36);
  toque3(BTN3, 41);
  toque4(BTN4, 43);
  toque5(BTN5, 48);
  toque6(BTN6, 55);
  toque7(BTN7, 60);
  break;
  case 2:
  toque1(BTN1, 65);
  toque2(BTN2, 73);
  toque3(BTN3, 82);
  toque4(BTN4, 87);
  toque5(BTN5, 97);
  toque6(BTN6, 110);
  toque7(BTN7, 121);
  break;
  case 3:
  toque1(BTN1, 130);
  toque2(BTN2, 146);
  toque3(BTN3, 164);
  toque4(BTN4, 174);
  toque5(BTN5, 196);
  toque6(BTN6, 220);
  toque7(BTN7, 242);
  break;
  case 4:
  toque1(BTN1, 261);
  toque2(BTN2, 293);
  toque3(BTN3, 329);
  toque4(BTN4, 349);
  toque5(BTN5, 391);
  toque6(BTN6, 440);
  toque7(BTN7, 485);
  break;
  case 5:
  toque1(BTN1, 523);
  toque2(BTN2, 587);
  toque3(BTN3, 659);
  toque4(BTN4, 698);
  toque5(BTN5, 783);
  toque6(BTN6, 880);
  toque7(BTN7, 971);
  break;
  case 6:
  toque1(BTN1, 1046);
  toque2(BTN2, 1174);
  toque3(BTN3, 1318);
  toque4(BTN4, 1396);
  toque5(BTN5, 1568);
  toque6(BTN6, 1760);
  toque7(BTN7, 1943);
  break;
  case 7:
  toque1(BTN1, 2093);
  toque2(BTN2, 2349);
  toque3(BTN3, 2637);
  toque4(BTN4, 2793);
  toque5(BTN5, 3136);
  toque6(BTN6, 3520);
  toque7(BTN7, 3886);
  break;
  case 8:
  toque1(BTN1, 4186);
  toque2(BTN2, 4698);
  toque3(BTN3, 5274);
  toque4(BTN4, 5587);
  toque5(BTN5, 6271);
  toque6(BTN6, 7040);
  toque7(BTN7, 7772);
  break;
  case 9:
  toque1(BTN1, 8372);
  toque2(BTN2, 9397);
  toque3(BTN3, 10548);
  toque4(BTN4, 11175);
  toque5(BTN5, 12544);
  toque6(BTN6, 14080);
  toque7(BTN7, 15546);
  break;
  }
}