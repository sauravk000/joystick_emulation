// Space, W, A, S, D in order 
const int buttonsPins[] = {3,4,5,6,7};
const int SIZE = 5;
const int analogXPin = A3;
const int analonYPin = A2;

int initialX, initialY;

void setup() {

  for(int i = 0;i<SIZE;i++) {
    pinMode(buttonsPins[i], INPUT);
  }  
  Serial.begin(115200);
  initialX = analogRead(A2);
  initialY = analogRead(A3);

}

void loop() {
    int x_value = analogRead(A2)-initialX;
    int y_value = analogRead(A3)-initialY;
    Serial.print("S");
    for(int i = 0;i<SIZE;i++) {
      Serial.print(String(digitalRead(buttonsPins[i])));
      Serial.print(",");
    }
    Serial.println(String(x_value)+ "," + String(y_value)); 
   delay(10);
}
