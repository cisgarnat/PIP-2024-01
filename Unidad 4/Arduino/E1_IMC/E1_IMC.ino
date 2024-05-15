int estado = 0;
float peso;
float altura;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  if (estado == 0) {
    Serial.println("Ingrese su peso (en kg):");
    estado++;
  } else if (estado == 1) {
    if (Serial.available() > 0) {
      peso = Serial.readString().toFloat();
      estado++;
    }
  } else if (estado == 2) {
    Serial.println("Ingrese su altura (en metros):");
    estado++;
  } else if (estado == 3) {
    if (Serial.available() > 0) {
      altura = Serial.readString().toFloat();
      estado++;
    }
  } else if (estado == 4) {
    float imc = peso / (altura * altura);
    Serial.println("Su índice de masa corporal (IMC) es: " + String(imc));
    estado++;
  } else if (estado == 5) {
    Serial.println("¿Desea calcular otro IMC? (1=Sí, 0=No)");
    estado++;
  } else if (estado == 6) {
    if (Serial.available() > 0) {
      int v = Serial.readString().toInt();
      if (v == 1) {
        estado = 0;
      } else {
        estado++;
      }
    }
  } else if (estado == 7) {
    Serial.println("Acabando el programa");
  }
  
  delay(100);
}
