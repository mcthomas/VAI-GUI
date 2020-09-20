

int brightness = 0;

void setup()
{
  pinMode(9, OUTPUT);
  pinMode(7, OUTPUT);
  Serial.begin(9600);	}
char a;
void loop()
{a=Serial.read();
  if( a=='1'){
  analogWrite(9, 255);
Serial.println("led1 on");}
  if (a=='2'){
  analogWrite(9, 0);
Serial.println("led1 off");}
  if (a=='3'){
  analogWrite(7, 255);
Serial.println("led2 on");}
  if (a=='4'){
  analogWrite(7, 0);
Serial.println("led2 on");}
}