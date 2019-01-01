import cv2
import numpy as np


highDiff = 60
toLeft = 125
redpackList = []

receive = cv2.imread('./rece1.png')
receive_gray = cv2.cvtColor(receive,cv2.COLOR_BGR2GRAY)


template = cv2.imread('./receive_tmp.jpg', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(receive_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold )


for pt in zip(*loc[::-1]):
    cv2.rectangle(receive, pt, (pt[0]+w, pt[1]+h), (0,255,0), 2)
    redpackList.append((pt[0], pt[1]))

for item in redpackList:
    (itemx, itemy) = item
    print(receive[itemy - highDiff, toLeft])


# cv2.imwrite('./output.jpg', receive)





