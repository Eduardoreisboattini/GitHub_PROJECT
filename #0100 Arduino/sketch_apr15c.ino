//This code sets up a two-digit countdown timer along with a tri-color traffic light. 
//The traffic light changes its colors based on the remaining time, 
//with red indicating less than 10 seconds, yellow indicating less than 30 seconds, and green indicating more than 30 seconds. 
//The countdown timer is displayed on two 7-segment displays.

// Define pin numbers for the traffic lights
const int redPin = 10;
const int yellowPin = 9;
const int greenPin = 8;

// Define pin numbers for the 7-segment display
const int segmentPins[] = {2, 3, 4, 5, 6, 7, 13, 12}; // Pins for segments A, B, C, D, E, F, G, DP (in order)
const int digitPins[] = {11, 13}; // Pins for digit selection (2 digits)

// Define the countdown duration in seconds
const int countdownDuration = 60; // 1 minute

void setup() {
  // Initialize the traffic light pins as outputs
  pinMode(redPin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  
  // Initialize the 7-segment display pins as outputs
  for (int i = 0; i < 8; i++) {
    pinMode(segmentPins[i], OUTPUT);
  }
  for (int i = 0; i < 2; i++) {
    pinMode(digitPins[i], OUTPUT);
  }
}

void loop() {
  // Start the countdown
  int remainingSeconds = countdownDuration;
  while (remainingSeconds > 0) {
    // Update the display
    displayNumber(remainingSeconds);
    
    // Update the traffic lights
    if (remainingSeconds <= 10) {
      digitalWrite(redPin, HIGH);
      digitalWrite(yellowPin, HIGH);
      digitalWrite(greenPin, LOW);
      delay(1000); // Blink every second
      digitalWrite(redPin, LOW);
      digitalWrite(yellowPin, LOW);
      delay(1000); // Blink every second
    } else if (remainingSeconds <= 30) {
      digitalWrite(redPin, LOW);
      digitalWrite(yellowPin, HIGH);
      digitalWrite(greenPin, LOW);
      delay(1000); // Blink every second
      digitalWrite(yellowPin, LOW);
      delay(1000); // Blink every second
    } else {
      digitalWrite(redPin, LOW);
      digitalWrite(yellowPin, LOW);
      digitalWrite(greenPin, HIGH);
      delay(1000); // Blink every second
      digitalWrite(greenPin, LOW);
      delay(1000); // Blink every second
    }
    
    remainingSeconds--;
  }
}

void displayNumber(int number) {
  int digit1 = number / 10;
  int digit2 = number % 10;
  
  // Display the first digit
  digitalWrite(digitPins[0], LOW);
  displayDigit(digit1);
  delay(5); // Delay for persistence of vision
  
  // Display the second digit
  digitalWrite(digitPins[0], HIGH);
  digitalWrite(digitPins[1], LOW);
  displayDigit(digit2);
  delay(5); // Delay for persistence of vision
  digitalWrite(digitPins[1], HIGH);
}

void displayDigit(int digit) {
  // Define common-cathode 7-segment display patterns for numbers 0 to 9
  byte patterns[] = {
    B11111100, // 0
    B01100000, // 1
    B11011010, // 2
    B11110010, // 3
    B01100110, // 4
    B10110110, // 5
    B10111110, // 6
    B11100000, // 7
    B11111110, // 8
    B11110110  // 9
  };
  
  // Output the pattern for the given digit
  for (int i = 0; i < 8; i++) {
    digitalWrite(segmentPins[i], bitRead(patterns[digit], i));
  }
}

