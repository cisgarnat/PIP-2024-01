int estado = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

int x1;
int x2;
int y1;
int y2;
void loop() {
  // put your main code here, to run repeatedly:
  if (estado == 0 || estado == 1) {
    
  Serial.println("Ingresa coordenadas A (X,Y)");
    if (Serial.available() > 0) {
      int v = Serial.readString().toInt();
      if (estado == 0) {
        x1 = v;
      } else {
        y1 = v;
      }
      estado++;
    }
  }
    else if (estado == 2 || estado == 3) {
    if (Serial.available() > 0) {
     
     Serial.println("Ingresa coordenadas B (X,Y)");
      int v = Serial.readString().toInt();
      if (estado == 2) {
        x2 = v;
      } else {
        y2 = v;
      }
      estado++;
    }
  } else if (estado == 4) {
    int x = (x1+x2)/2;
    int y = (y1+y2)/2;
    Serial.println("Punto Medio entre punto A y B (" + String(x)+"," + String(y)+")");
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
