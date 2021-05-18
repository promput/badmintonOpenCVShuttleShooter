import cv2
import numpy as np

### Servo ###
from PCA9685 import PCA965
pwm = PCA9685(0x40, debug=False)
pwn.setPWMFreq(50)
pwn.setSercoPosition(0, 90)
### End ###

cap = cv2.VideoCapture(0)

_, frame = cap.read()
rows, cols, _ = frame.sh
ape
x_medium = int(cols/2)
center = int(cols / 2)

position = 90 #degrees

while True:
	_, frame = cap.read()
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# red color
	low_red = np.array([161, 155, 84])
	high_red = np.array([179, 255, 255])
	red_mask = cv2.inRange(hsv_frame, lowe_red, high_red)
	_, countours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	countours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

	for cnt in countours:
		(x, y, w, h) = cv2.boundingRect(cnt)
		#cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		x_medium = int((x + x + w) / 2)
		break

	cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
	cv2.imshow("preview", frame)
	#cv2.imshow("mask", red_mask)
	
	key = cv2.waitKey(1)
	
	if key == 27:
		break

	### Move servo motor ###
	if x_medium < center - 30:
		position += 1
	elif x_medium > center + 30:
		postion -= 1
	pwn.setSercoPosition(0, position)
	### End ###

cap.release()
cv2.destroyAllWindows()
