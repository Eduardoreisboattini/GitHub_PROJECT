// Traffic Light Simulation
//This code simulates the behavior of a traffic light,
// with each light staying on for a specified duration. 
//The red light stays on for 5 seconds, then transitions to red and yellow for 2 seconds, 
//then green for 5 seconds, and finally yellow for 2 seconds before looping back to the red light.

// Define pins for the LEDs
const int redPin = 13;
const int yellowPin = 12;
const int greenPin = 11;

void setup() {
  // Initialize the LED pins as outputs
  pinMode(redPin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
}

void loop() {
  // Red light
  digitalWrite(redPin, HIGH);
  digitalWrite(yellowPin, LOW);
  digitalWrite(greenPin, LOW);
  delay(5000); // 5 seconds
  
  // Red and Yellow light (transition)
  digitalWrite(redPin, HIGH);
  digitalWrite(yellowPin, HIGH);
  digitalWrite(greenPin, LOW);
  delay(2000); // 2 seconds
  
  // Green light
  digitalWrite(redPin, LOW);
  digitalWrite(yellowPin, LOW);
  digitalWrite(greenPin, HIGH);
  delay(5000); // 5 seconds
  
  // Yellow light
  digitalWrite(redPin, LOW);
  digitalWrite(yellowPin, HIGH);
  digitalWrite(greenPin, LOW);
  delay(2000); // 2 seconds
}