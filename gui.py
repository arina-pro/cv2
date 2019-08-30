import numpy as np
import cv2

img = cv2.imread('city.png', 1)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)

k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('city_gray.png', img)