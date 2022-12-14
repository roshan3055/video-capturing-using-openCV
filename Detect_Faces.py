#!/usr/bin/env python
# coding: utf-8


#FACE DETECTION 

import cv2, time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

check, frame = video.read()

gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in faces:
    frame=cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
    
time.sleep(3)

cv2.imshow("capturing", frame)    

cv2.waitKey(0)


video.release()

cv2.destroyAllWindows()





