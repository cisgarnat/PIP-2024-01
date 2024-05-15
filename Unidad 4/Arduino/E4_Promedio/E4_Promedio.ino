int estado = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

int a;
int b;
int c;
int d;
void loop() {
  // put your main code here, to run repeatedly:
  if (estado == 0 || estado == 1 || estado == 2 || estado == 3) {
    
  Serial.println("Ingresa 4 numeros");
    if (Serial.available() > 0) {
      int v = Serial.readString().toInt();
    if (estado == 0) {
        a = v;
        estado++;
      } else if (estado == 1){
        b = v;
        estado++;
      }
      else if (estado == 2){
        c = v;
        estado++;
      }
      else {
        d = v;
        estado++;
      }
    }
  
    
  } else if (estado == 4) {
    int r = (a+b+c+d)/4;
    Serial.println("Promedio: " + String(r));
    estado = 5;
    //Serial.println(estado);
  } else if (estado == 5) {
    Serial.println("Desea repetir?....(1=SI, 0=NO)");
    estado++;
  } else if (estado == 6) {
    if (Serial.available() > 0) {
      int v = Serial.readString().toInt();
      if (v == 1) {
        estado = 0;
      } else {
        estado = 5;
      }
    }
  }
  delay(100);
}
