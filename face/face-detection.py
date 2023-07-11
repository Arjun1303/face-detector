import cv2
import numpy as np
#face detection in the video
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#create video capture and read from input file
cap = cv2.VideoCapture("orange.mp4")

while cap.isOpened():
    
    _, img = cap.read()
    
    #convert the video into gray video
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detect face in the video
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    #draw rectangle box around the faces
    
    for(X, Y , W ,h) in faces:
        cv2.rectangle(img, (X,Y), (X+W, Y+h), (255, 0 , 0), 2)
    #display resulting frame
        
    cv2.imshow('img', img)
    
    # press Q on keyboard to exit
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()

#close all frames
cv2.destroyAllWindows()