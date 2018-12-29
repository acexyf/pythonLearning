import cv2


imgPath =  "./img1.jpeg"
cascPath = "./haarcascade_frontalface_default.xml"


faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imgPath)
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray_img,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30)
)
print(faces)
print("Found {0} faces!".format(len(faces)))


for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0), 2)


cv2.imwrite('output.jpg',image)

