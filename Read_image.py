#READ IMAGES AND DETEECT THE FACES

import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread("D:\\Screen.png")
resized = cv2.resize(img, (800,600))

gray_img = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    resized= cv2.rectangle(resized, (x,y), (x+w,y+h), (0,255,0), 2)



cv2.imshow("hero", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()