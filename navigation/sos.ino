int pin8 = 8;
int sensor = A0;
int sensorValue = 0;

int buttonState = 0;

void setup() {
  pinMode(pin8, OUTPUT);
  Serial.begin(9600);
  pinMode(2, INPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  sensorValue = analogRead(sensor);
  //Serial.println(sensorValue, DEC);
  if (sensorValue > 800) {
    digitalWrite(pin8, HIGH);
    Serial.println("sending exit command");
  }
  if  (sensorValue < 800){
    digitalWrite(pin8, LOW);
  }

  buttonState = digitalRead(2);
  if (buttonState == HIGH) {
    digitalWrite(13, HIGH);
    Serial.println("Alerting neghbors");
  } else {
    digitalWrite(13, LOW);
  delay(10); }
}