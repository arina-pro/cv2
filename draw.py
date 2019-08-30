import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)

img = cv2.circle(img, (256, 256), 250, (255, 255, 255), -1, cv2.LINE_AA)

img = cv2.line(img, (256, 0), (256, 511), (0, 0, 0), 20)

img = cv2.rectangle(img, (156, 156), (356, 356), (200,255,200), -1)

img = cv2.ellipse(img, (156, 156), (100, 50), 0, 0, 180, (200, 225, 255), -1, cv2.LINE_AA)

pts = np.array([[310,335],[320,330],[370,320],[356,356]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 255, 225), 20, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)