int estado = 0;
float a, b;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  if (estado == 0 || estado == 1 ){
    if (Serial.available() > 0) {
      Serial.println("Ingrese la altura y la base de un rectangulo:");
      float v = Serial.parseFloat(); 
      if (estado == 0) {
        a = v;
        estado ++; 
      } else if (estado == 1) {
        b = v;

        float area = b * a ;

        Serial.print("El Area del rectangulo es: "+ String(area));
        estado ++;
      }
    }
  }else if(estado ==2){
    Serial.println("Desea repetir?....(1=SI, 0=NO)");
    estado++;
  }else if(estado == 3){
    if(Serial.available()>0){
        int v = Serial.readString().toInt();
        if(v==1){
          estado = 0;
        } else {
          estado = 2; 
        }
      }
    }

  delay(100);
}
