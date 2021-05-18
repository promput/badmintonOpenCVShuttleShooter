#include<Servo.h> //Using servo library to control ESC

Servo esc1;
Servo esc2; //Creating a servo class with name as esc

void setup()

{
  esc1.attach(8); //Specify the esc signal pin,Here as D8
  esc2.attach(7);
  
  esc1.writeMicroseconds(1000); //initialize the signal to 1000
  esc2.writeMicroseconds(1000);
  
  Serial.begin(9600);
}

void loop()

{
  int val; //Creating a variable val
  int val1;
  int val2;

  val= analogRead(A0); //Read input from analog pin a0 and store in val
  val1= map(val, 0, 1023/1.22,1000/1.22,2000/1.22);
  val2= map(val, 0, 1023/2,1000/2,2000/2);
  Serial.println(val1);//mapping val to minimum and maximum(Change if needed)
  
  esc1.writeMicroseconds(val1); //using val as the signal to esc
  esc2.writeMicroseconds(val2); //using val as the signal to esc
}
