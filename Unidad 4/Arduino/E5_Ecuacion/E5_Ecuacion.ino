int estado = 0;
float m, x, b, y;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  if (estado == 0 || estado == 1 || estado == 2) {
    if (Serial.available() > 0) {
      Serial.println("Ingrese el valor de M,X y Y:");
      float v = Serial.parseFloat(); 
      if (estado == 0) {
        m = v;
        estado ++; // Pasar al siguiente estado
      } else if (estado == 1) {
        x = v;
        estado ++; // Pasar al siguiente estado
      } else if (estado == 2) {
        b = v;
        // Calcular y = mx + b
        float y = m * x + b;

        // Mostrar el resultado
        Serial.print("El resultado de y es"+ String(y));
        estado ++;
      }
    }
  }else if(estado ==3){
    Serial.println("Desea repetir?....(1=SI, 0=NO)");
    estado++;
  }else if(estado == 4){
    if(Serial.available()>0){
        int v = Serial.readString().toInt();
        if(v==1){
          estado = 0;
        } else {
          estado = 3; 
        }
      }
    }

  delay(100);
}
