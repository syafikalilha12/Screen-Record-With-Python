from PIL.Image import fromarray
import numpy as np 
import cv2 
import pyscreenshot as ImageGrab
from numpy.core.numeric import convolve
import imutils
while True:
    img = ImageGrab.grab()
	img_np = np.array(img)
	frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
	low = np.array([20,100,100])
	high = np.array([20,255,255])
	mask = cv2.inRange(frame,low,high)
	if cv2.waitKey(1) == 27:
		break
cv2.release()
cv2.destroyAllWindows()