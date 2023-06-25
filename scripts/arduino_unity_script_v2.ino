const int xAxisPin = A0; //Set A0 as X-axis
const int yAxisPin = A1; //Set A1 as Y-axis
const int buttonPin = 2; //Set digital pin 2 as button
int xCount, yCount;

void setup() {
  pinMode(xAxisPin, INPUT); 
  pinMode(yAxisPin, INPUT); 
  pinMode(buttonPin, INPUT_PULLUP); 

  Serial.begin(9600);
}

void loop() {
  int readX = analogRead(xAxisPin) - 517; // read X axis value 0..1023 - 517 to round it close to 0
  int readY = analogRead(yAxisPin) - 517; // read Y axis value 0..1023 - 512 to round it close to 0
  int readButton = 0;

  readButton |= ((digitalRead(buttonPin) == LOW) ? 1 : 0) << 0;

  if (readX < -10) xCount = 0;  //joystick has off set of +/-8 which causes it to drift this negates that
  else if (readX > 10) xCount = 2;  //turn analogue value into integer 0, 1 or 2 depending on state                    
  else xCount = 1;
 
  if (readY < -10) yCount = 0; 
  else if (readY > 10) yCount = 2;                      
  else yCount = 1;
 
  //Print format xCount,yCount,readButton -> S1,1,0
  Serial.print(xCount);
  Serial.print(",");
  Serial.print(yCount);
  Serial.print(",");
  Serial.println((readButton));

  delay(100);
}