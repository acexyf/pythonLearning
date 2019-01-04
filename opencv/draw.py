import numpy as np
import cv2

img = cv2.imread('./bg.jpg',cv2.IMREAD_COLOR)
pts = np.array([[300,400], [400,600], [600,360]], np.int32)
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.line(img, (0,0),(150,150),(255,0,0),5)
cv2.rectangle(img, (3, 160), (153,320),(255,0,0),3)
cv2.circle(img, (200, 400),50,(255,0,0), -1)
cv2.polylines(img, [pts], True, (255,0,0),2)
cv2.putText(img, 'My Text!', (300,700), font, 1, (255,0,0),1,cv2.LINE_AA)

cv2.imwrite('./new.jpg',img)


