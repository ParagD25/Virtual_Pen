import cv2
import numpy as np

capture=cv2.VideoCapture(0)


# yellow,blue,purple,green,orange
colors=[[20,112,139,64,255,255],
[84,87,81,104,255,255],
[105,43,80,137,140,200],
[56,58,120,85,255,255],
[0,82,150,15,210,255]]

colorVal=[[34,212,203],
    [255,204,0],
    [105,17,88],
    [27,122,32],
    [47,47,237]
]


def findColors(img,colors,colorVal):
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    for color in colors:
        lower=np.array(color[0:3])
        upper=np.array(color[3:6])

        mask=cv2.inRange(imgHSV,lower,upper)
        x,y=getContours(mask)

        cv2.circle(frame2,(x,y),5,colorVal[count],-1)
        count+=1
        # cv2.imshow(str(color[0]),mask)

def getContours(frame):
    contours,hierarchy=cv2.findContours(frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv2.contourArea(cnt)

        if area>500:
            # cv2.drawContours(frame2,cnt,-1,(255,0,0),3)

            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)

            x,y,w,h=cv2.boundingRect(approx)
    return x+w//2,y


while True:
    ret,frame=capture.read()
    frame2=frame.copy()

    findColors(frame,colors,colorVal)

    cv2.imshow("Pen",frame2)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()