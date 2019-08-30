import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#cap.set(3, 320)
#cap.set(4, 240)

fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('vert.avi', fourcc, 20.0, (int(cap.get(3)),int(cap.get(4))), isColor = False)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame,0)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        out.write(frame)

        cv2.imshow('frame', gray)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()

cap2 = cv2.VideoCapture('vert.avi')

while(cap2.isOpened()):
    ret, frame = cap2.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap2.release()