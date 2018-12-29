import numpy as np
import time
import datetime
import cv2

# imgRGB = np.array([62,62,255])
# redRGB = [62,62,251]
# print(np.array_equal(imgRGB,redRGB))

# print(datetime.datetime.now().strftime('%Y-%m-%d'))

# print(str(int(time.time())))


img = cv2.imread('../opencv/rece1.png')

list = [1,2,3,4,5,6]
newList = []

for item in range(5):
    print(item)
    if item == 3:
        break;




print(newList)


