#include <NewPing.h> // Include library for ultrasonic sensor

// Stepper Motor X
const int stepPin = 2; // X.STEP
const int dirPin = 5;  // X.DIR

// Ultrasonic sensor pins
const int trigPin = 31; // Ultrasonic sensor trigger pin
const int echoPin = 32; // Ultrasonic sensor echo pin

// Define the maximum distance for obstacle detection in inches
const int maxDistanceInches = 10;
// Define the maximum distance in centimeters (converted from inches)
const int maxDistanceCM = maxDistanceInches * 2.54;

// Initialize NewPing sensor
NewPing sonar(trigPin, echoPin, maxDistanceCM);

void setup() {
  pinMode(stepPin, OUTPUT); // Sets the stepper motor step pin as output
  pinMode(dirPin, OUTPUT);  // Sets the stepper motor direction pin as output
}

void loop() {
  unsigned int distance = sonar.ping_cm(); // Read the distance from the ultrasonic sensor

  // Check if an obstacle is within the specified range
  if (distance <= maxDistanceCM && distance > 0) {
    // Stop the stepper motor
    digitalWrite(stepPin, LOW);
    digitalWrite(dirPin, LOW);

    // Wait for 12 seconds before moving again
    delay(12000);

    // Move stepper in reverse direction after waiting
    digitalWrite(dirPin, HIGH); // Set direction
    for (int i = 0; i < 700; i++) {
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(1200);
      digitalWrite(stepPin, LOW);
      delayMicroseconds(1200);
    }
  } else {
    // Move the stepper motor forward
    digitalWrite(dirPin, HIGH); // Set direction

    // Make 200 pulses for one rotation (depends on your motor driver setup)
    for (int x = 0; x < 200; x++) {
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(1200);
      digitalWrite(stepPin, LOW);
      delayMicroseconds(1200);

      // Check ultrasonic sensor output every 40 steps
      if (x % 40 == 0) {
        distance = sonar.ping_cm(); // Update distance
        if (distance <= maxDistanceCM && distance > 0) {
          // Stop the stepper motor if obstacle detected
          digitalWrite(stepPin, LOW);
          digitalWrite(dirPin, LOW); // You may need to adjust depending on wiring
          break; // Exit the loop early
        }
      }
    }
    // Optional pause between rotations
    // delay(2000);
  }
}
