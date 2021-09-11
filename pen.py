import cv2

fheight=480
fwidth=640
capture=cv2.VideoCapture(1)

capture.set(3,fwidth)
capture.set(4,fheight)
capture.set(10,150)

while True:
    win,img=capture.read()
    cv2.imshow("Pen",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break