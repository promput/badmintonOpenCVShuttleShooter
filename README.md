# badmintonOpenCVShuttleShooter
I have made an IoT device that look around the room for people and shoot out badminton shuttle when human is present in its vision.
![Test Image 1](/figures/opencv.png.png)
![Test Image 1](/figures/prototype.png)

### How to Run
There are two main control embedded systems in this project. All the .py code will be run on the Raspberry Pi 3 utilzing the open CV from Tensorflow. It will also create artificial PWM for the servos. The brushless motor however, will be controlled by the Arduino with .ino suffix. 
1. Upload servos extension for Uno in the zip file to the Arduino app.
2. Upload .ino file to the Arduino.
3. Upload .py file to the Raspberry Pi.

### Note
I still do want to find the SD car that my combine.py, which is the file that combine the servos control with the openCV control.
