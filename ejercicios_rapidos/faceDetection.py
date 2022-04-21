import cv2
import numpy as np


def zoom(img, zoom_factor=2):
    return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)


img = cv2.imread("caras.png", 1)
#img = cv2.resize(img, (1100, 900))
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)

print(img)
print('-'*60)
print(img.shape)

#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
print(cv2.data.haarcascades)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #path for face cascade, path where it is stored specific classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(grayFrame, 1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    car = cv2.waitKey(1)

    if (car == ord('e')):
        break

    elif (car == ord('o')):
        pass

    elif (car == ord('i')):
        frame = zoom(frame, 2)

    cv2.imshow('Frame', frame)

cap.release()
cv2.destroyAllWindows()