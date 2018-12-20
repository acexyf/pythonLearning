import cv2

img = cv2.imread('./wenting.jpg')

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('wsc-gray.jpg',img)

cv2.threshold(img, 550, 550, 0, img) 
cv2.imwrite('wsc-two-value.jpg',img)