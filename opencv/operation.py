import cv2
import numpy as np

bgImg = cv2.imread('./regist-top-new.jpg')
heartImg = cv2.imread('./heart.png')

# newImg = bgImg + heartImg

newImg = cv2.addWeighted(bgImg, 0.6, heartImg, 0.4, 0)


cv2.imwrite('./new.jpg',newImg)




