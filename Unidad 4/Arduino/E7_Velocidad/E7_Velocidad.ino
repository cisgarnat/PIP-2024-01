int estado = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

int d;
int t;


void loop() {
  // put your main code here, to run repeatedly:
  if (estado == 0) {
     Serial.println("Ingresa la distancia");
     delay(1500);
    if (Serial.available() > 0) {
     
      d = Serial.readString().toInt();

      Serial.println("Distancia = " + String(d));
      estado++;
      Serial.println("Estado " + String(estado));
    }
  } else if (estado == 1) {
    Serial.println("Ingresa el tiempo");
    delay(1500);
    if (Serial.available() > 0) {
      t = Serial.readString().toInt();
      Serial.println("Tiempo = " + String(t));
      estado++;
      Serial.println("Estado "+String(estado));
    }
  } else if (estado == 2) {
      float v = (float)d / t;
      Serial.println("La velocidad con distancia: " + String(d) + " y tiempo: " + String(t) + " = " + String(v));
      estado = 0;
    
  }
}
