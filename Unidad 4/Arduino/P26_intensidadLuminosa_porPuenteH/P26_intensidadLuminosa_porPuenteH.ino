//l298d -- modulo
// ---2 puentes h

//ENA ---velocidad de giro
//IN1 -- sentido de giro
//IN2
//OUT1
//OUT2

//ENB
//IN3
//IN4
//OUT3
//OUT4

int ENA = 3;
int in1 = 5;

//conectamos al motor
// out1 out2 se conectan directamente del puente h al motor

void setup() {
  // put your setup code here, to run once:
  pinMode(in1, OUTPUT);

  //ENA ni lleva pinmode por que es un PWM

  Serial.begin(9600);
  Serial.setTImeout(10);
  
}

void loop() {
  // put your main code here, to run repeatedly:

  if(Serial.available()>0){
    int v =Serial.readString().toInt();
      digitalWrite(in1,0);
      analogWrite(ENA,v);
      
    }
  delay(100);

}
