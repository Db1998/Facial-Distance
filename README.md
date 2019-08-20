# Simultaneous Face tracking and Distance measurement using OpenCV library in Python

Implemented my idea of measuring the facial distance using only a single camera, thereby eliminating the requirement for any proximity sensor or extra camera, with the OpenCV library in Python.
![](Screenshot%20(33).png)
## OpenCV
OpenCV is Computer Vision library of programming functions mainly aimed at real-time computer vision.
## Focal length
Calculated focal length of the camera using a set of measured distances and the corresponding number of pixels in face region of the image. Local webcam in the laptop was used.
focal length = (No. of pixels in the width of face image) * (Width of the face) / (Distace of face from camera)
## Face Detection
Used the standard face detection Haar cascades available in OpenCV library to deetect human faces in real-time.
## Facial distance
Using the calculated focal length of the webcam and face-detection in real-time, facial distance from camera can be calculated and displayed in real-time.
Distance = (No. of pixels in the width of face image) * (Width of the face) / (focal-length)
## Resources
www.opencv.org
