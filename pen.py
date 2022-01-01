import cv2
import numpy as np

capture=cv2.VideoCapture(0)

color=[]


def findColors(img):
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    

def findContours():
    pass


while True:
    ret,frame=capture.read()
    cv2.imshow("Pen",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()