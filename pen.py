import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(3,1250)
cap.set(4,1750)

Col=[[20,112,139,64,255,255],
[84,87,81,104,255,255],
[105,43,80,137,140,200],
[56,58,120,85,255,255],
[0,82,150,15,210,255]]

ColVal=[[34,212,203],
    [255,204,0],
    [105,17,88],
    [27,122,32],
    [47,47,237]]

pnts=[]

def findColor(frame,Col,ColVal):
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    count=0
    pnts=[]

    for color in Col:
        lower=np.array(color[0:3])
        upper=np.array(color[3:6])
        mask=cv2.inRange(frameHSV,lower,upper)

        x,y=getContours(mask)
        cv2.circle(frame2,(x,y),12,ColVal[count],-1)

        if x!=0 and y!=0:
            pnts.append([x,y,count])
        count+=1

    return pnts

def getContours(frame):
    contours,hierarchy=cv2.findContours(frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0

    for cnt in contours:
        area=cv2.contourArea(cnt)

        if area>350:
            # cv2.drawContours(frame2,cnt,-1,(255,0,0),3)

            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)

    return x+w//2,y

def drawOnCanvas(pnts,ColVal):
    for point in pnts:
        cv2.circle(frame2,(point[0],point[1]),10,ColVal[point[2]],-1)

while True:
    ret,frame=cap.read()
    frame2=frame.copy()
    newPoints=findColor(frame,Col,ColVal)

    if len(newPoints)!=0:
        for newP in newPoints:
            pnts.append(newP)

    if len(pnts)!=0:
        drawOnCanvas(pnts,ColVal)

        cv2.imshow('Result',frame2)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

cap.release()
cv2.destroyAllWindows()