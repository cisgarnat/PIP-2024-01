int led = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(led,OUTPUT);
 }

int valor;
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    val = Serial.readString().toInt();
    digitalWrite(led,valor);
    if(valor ==1){
      Serial.println("Led Prendido");
      }
    else[]
  }
}
