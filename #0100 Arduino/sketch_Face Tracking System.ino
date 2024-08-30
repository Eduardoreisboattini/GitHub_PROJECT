#include <opencv2/opencv.hpp>
#include <Servo.h>

using namespace cv;

Servo servoHorizontal;
Servo servoVertical;

int x = 90;
int y = 90;

void setup() {
  servoHorizontal.attach(9);
  servoVertical.attach(10);
}


/**
 * @brief Main loop of the program.
 *
 * Captures frames from the default camera, detects faces using the
 * OpenCV cascade classifier, and moves the servos to the position of
 * the detected face.
 */

void loop() {
  Mat frame;
  VideoCapture cap(0);
  
  if (!cap.isOpened()) {
    Serial.println("Cannot open the video camera");
    return;
  }
  
  while (true) {
    if (!cap.read(frame)) {
      Serial.println("Cannot read a frame from video stream");
      break;
    }
    
    CascadeClassifier faceDetector;
    faceDetector.load("haarcascade_frontalface_default.xml");
    
    vector<Rect> faces;
    faceDetector.detectMultiScale(frame, faces);
    
    for (int i = 0; i < faces.size(); i++) {
      Point center(faces[i].x + faces[i].width / 2, faces[i].y + faces[i].height / 2);
      
      x = map(center.x, 0, frame.cols, 0, 180);
      y = map(center.y, 0, frame.rows, 0, 180);
      
      servoHorizontal.write(x);
      servoVertical.write(y);
    }
  }
}
