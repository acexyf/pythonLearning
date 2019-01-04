import cv2
import numpy as np



img = cv2.imread('./girl.jpeg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# retval, threshold = cv2.threshold(img_gray, 150,255,cv2.THRESH_BINARY)

# 自适应阀值二值化
threshold = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)


cv2.imwrite('./new.jpg', threshold)


