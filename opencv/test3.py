import cv2

color_img = cv2.imread('./receive.png')

print(color_img.shape)

gray_img = cv2.imread('./receive.png',cv2.IMREAD_GRAYSCALE)
print(gray_img.shape)

cv2.imwrite('new_gray.png',gray_img)

reload_gray_img = cv2.imread('./new_gray.png')
print(reload_gray_img.shape)

