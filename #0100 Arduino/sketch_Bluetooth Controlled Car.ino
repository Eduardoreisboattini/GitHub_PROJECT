#include <AFMotor.h>

#define FORWARD 1
#define BACKWARD 2
#define LEFT 3
#define RIGHT 4
#define STOP 5

AF_DCMotor motor1(1, MOTOR12_1KHZ);
AF_DCMotor motor2(2, MOTOR12_1KHZ);

char command;



/**
 * @brief Initializes the serial communication at 9600 bps and sets the speed of
 *        both motors to 150.
 */

void setup() {
  Serial.begin(9600);
  motor1.setSpeed(150);
  motor2.setSpeed(150);
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.read();

    switch (command) {
      case 'f':
        motor1.run(FORWARD);
        motor2.run(FORWARD);
        break;
      case 'b':
        motor1.run(BACKWARD);
        motor2.run(BACKWARD);
        break;
      case 'l':
        motor1.run(FORWARD);
        motor2.run(BACKWARD);
        break;
      case 'r':
        motor1.run(BACKWARD);
        motor2.run(FORWARD);
        break;
      case 's':
        motor1.run(RELEASE);
        motor2.run(RELEASE);
        break;
    }
  }
}
