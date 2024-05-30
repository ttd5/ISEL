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
/*
void distance(int pinTrig, int pinEcho, int rate) {
  unsigned int T = 1000000/rate;
  static unsigned long t0 = micros();
  static const int TRIGSTART = 0, TRIGSTOP = 1, ECHOSTART = 2, ECHOSTOP = 3;
  static int state = TRIGSTART;
  switch(state){
    //INICIAR SINAL DO TRIGGER
    case TRIGSTART:
      digitalWrite(pinTrig, HIGH);
      t0 = micros();
      state = TRIGSTOP;
    break;
  //PARAR SINAL DO TRIGGER
    case TRIGSTOP:
      if(micros() - t0 > T) {
        digitalWrite(pinTrig, LOW);
        state = ECHOSTART;           
      }
    break;
  //LIGAR ECHO
    case ECHOSTART:
      if(digitalRead(pinEcho) == HIGH) {
        t0 = micros();
        state = ECHOSTOP;
      }
    break;
  //RECEBER SINAL DO TRIGGER E DESLIGAR ECHO
    case ECHOSTOP:
      if(digitalRead(pinEcho) == LOW) {
        int d = (micros() - t0)/58.0;
        Serial.println(d);
        state = TRIGSTART;
      }
    break;
    }    
}

void printCSV(int rate, float val1, float val2) {
  unsigned int T = 1000 / rate;
  static unsigned long t0 = millis();
  static const int WAIT = 0, SEND = 1;
  static int state = WAIT;
  //ESPERA VALORES
  switch (state) {
    case WAIT:
      if(millis() - t0 > T) {
        state = SEND;
        t0 = millis();
      }
    break;
    //ENVIA VALORES PARA A CONSOLA
    case SEND:
      Serial.println(word(val1) + "\t" + word(val2));
      state = WAIT;
    break;      
  }
}

void melodia(int duration, int nota1, int nota2) {
  unsigned int T = duration;
  static unsigned long t0 = millis();
  static const int NOTA1 = 0, NOTA2 = 1;
  static int state = NOTA1;
  //TOCA NOTA 1
  switch (state) {
    case NOTA1:
      tone(3, nota1);    
      if(millis() - t0 > T) {
        noTone(3); //DESLIGA NOTA 1
        state = NOTA2;
        t0 = millis();
      }
    break;
   //TOCA NOTA 2
    case NOTA2:
      tone(3, nota2);
      if(millis() - t0 > T) {
        noTone(3); //DESLIGA NOTA 2
        state = NOTA1;
        t0 = millis();
      }
    break;  
   } 
}

int count = 0;
void contador(int pin) {
  static const int START = 0, STOP = 1;
  static int state = START;
  switch (state) {
  //QUANDO O BOTÃO NÃO É PREMIDO    
  case START:
    Serial.println("START");
      if(digitalRead(pin) == 1) {
        state = STOP;
      }
    break;
    //QUANDO O BOTÃO É PREMIDO
    case STOP:
      if(digitalRead(pin) == 0) {
        state = START;
        Serial.println("STOP");
      }
    //INCREMENTA O VALOR PELO TEMPO QUE É PREMIDO
      count++;
      Serial.println(count);
    break;
  }
}

void toque(int pinBotao) {
  int buttonPressed = 0;
  static const int START = 0, STOP = 1;
  static int state = START;
  //SE FOI CLICADO
  switch (state) {
    case START:
    buttonPressed = digitalRead(pinBotao);
      if(buttonPressed == LOW) {
        state = STOP;
        Serial.println("STOP");
      }
    break;
    //SE FOI LARGADO
    case STOP:
    buttonPressed = digitalRead(pinBotao);
    if(buttonPressed == HIGH) {
      state = START;
      Serial.println("START");
    }
    break;
  }
}

void gerador(int rate, int periodo, char tipoOnda) {
  unsigned int T = 1000 / rate;
  static unsigned long t1 = millis(), t0 = 0;
  static int state;
  static const int q = 0, s = 1, t = 2;
  //ESCOLHER OPÇÃO DO TIPO DE ONDA
  if (tipoOnda == 'q') {
    state = q;
  } else if (tipoOnda == 's') {
    state = s;
  } else if (tipoOnda == 't'){
    state = t;
  }
  
  switch (state) {
    //OPÇÃO QUADRADA
    case q:
    static const int UPPER = 0, DOWN = 1;
    static int bound = UPPER;
    switch(bound) {
      //QUANDO ESTÁ NO LIMITE SUPERIOR
      case UPPER:
      Serial.println(10.0);
      if(t1-t0 >= T/2) {
        t0 = t1;
        bound = DOWN;
      }
      //QUANDO ESTÁ NO LIMITE INFERIOR
      case DOWN:
      Serial.println(0.0);
      if(t1-t0 >= T/2) {
        t0 = t1;
        bound = UPPER;
      }
    break;
    }
    //OPÇÃO SINUSOIDAL
    case s:
      Serial.println(1.0*sin(2.0 * 3.14 * millis()));        
    break;
    
    //OPÇÃO TRIÂNGULAR
    case t:
      static const int ASC = 0, DESC = 1;
      int state = ASC; 
      static float amp = 0;      
      switch (state) {
        //QUANDO ESTÁ A ASCENDER
        case ASC: 
          t1 = millis();
          amp = (2 * (10.0/T))*(t1 - t0);
          Serial.println(amp);
          if(t1 - t0 >= T/2) {
            t0 = t1;
            state = DESC;
          }          
        break;
        //QUANDO ESTÁ A DESCENDER
        case DESC:
         t1 = millis();
          amp = (-2 * (10.0/T))*(t1 - t0) + 10;
          Serial.println(amp);
          if(t1 - t0 >= T/2) {
            t0 = t1;
            state = DESC;
          }           
        break;
      }     
    break;
  }
}
*/
int val = 0; 
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
#define BTN4 8
#define BTN5 10
#define BTN6 11
#define BTN7 12
#define PIEZO 3

void toque1(int pinBotao, int nota) {
  static int buttonPressed = 0;
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
  static int buttonPressed = 0;
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
  static int buttonPressed = 0;
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
  static int buttonPressed = 0;
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
  static int buttonPressed = 0;
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
  static int buttonPressed = 0;
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
  static int buttonPressed = 0;
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

void piano() {
  switch (val) {
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

//gerador(1, 100, 'q');
//contador(BTN1);
//melodia(5000, 100, 560);
//printCSV(2, digitalRead(BTN1), digitalRead(PINECHO));
//distance(PINTRIG, PINECHO, 10);
//toque(BTN1); 

//PROJETO PIANO
receiveInt();
piano();
}