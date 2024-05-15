int estado = 0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
delay(100);
}
double apotema;
double perimetro;
void loop() {
  // put your main code here, to run repeatedly:
  if(estado == 0 ){

     Serial.println("Ingresa el apotema");
     delay(1000);
    if(Serial.available()>0){
      apotema = Serial.readString().toDouble();
      Serial.println(String(apotema));
      estado ++ ;

     
    }
  }else if(estado == 1){
    Serial.println("Ingresa el perimetro");
     delay(1000);
    if(Serial.available()>0){
     
      perimetro = Serial.readString().toDouble();
      Serial.println(String(perimetro));
      estado ++ ;

     
    }
  }else if(estado == 2){
   double area = (apotema * perimetro)/2;
    Serial.println("El area del poligono regular = "+String(area) + "cm^2");
    estado = 0;
  }
}
