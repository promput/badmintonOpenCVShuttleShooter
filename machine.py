### Libraries ###
import numpy as np
import RPi.GPIO as GPIO
import time
### END ###

### Variable Setups ###
GPIO.setmode(GPIO.BOARD)
CPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50)
servo1.start(0)
CPIO.setup(11, GPIO.OUT)
servo2 = GPIO.PWM(13, 50)
servo2.start(0)
CPIO.setup(12, GPIO.OUT)
servo3 = GPIO.PWM(15, 50)
servo3.start(0) 
#servo1.ChangeDutyCycle(2+(angle/18))
angle1 = 0
angle2 = 0
angle3 = 0
### END ###

### Executions ###
try:
	inp = "h"
	while inp != "n":
		x = input("[y:start]/[n:end]")
		if x == "y":
			#bending the arm
			servo1.ChangeDutyCycle(2+(angle1/18)+5)
			time.sleep(0.3)
			#opening and close the claw
			servo2.ChangeDutyCycle(2+(angle2/18))
			timesleep(0.3)
			servo2.ChangeDutyCycle(2+(0/18))
			#bending the arm
			servo1.ChangeDutyCycle(2+(angle1/18)+5)
			time.sleep(0.3)
### END ###

### House Keeping ###
finally:
	cap.release()
	cv2.destroyAllWindows()
	servo1.stop()
	servo2.stop()
	servo3.stop()
	GPIO.cleanup()
### END ###