import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('test.jpg')
# zero signifies the camera to be used if multiple camera is connected
cap = cv2.VideoCapture(0)
#here we are adding this never ending loop as live video is nothing but
#a flow of continious image
while(True):
# Capture frame-by-frame
    ret, img = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces)>0:
        
       # run a video
       

cap.release()
cv2.destroyAllWindows()
