#Face and eye detection,
#also see: http://docs.opencv.org/trunk/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html
#Training:
#http://docs.opencv.org/doc/user_guide/ug_traincascade.html
#Gerald Schuller, Dec 2014

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


cap = cv2.VideoCapture(0)

while(True):
    [retval, frame] = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#Width of face at 1m distance (x-coordinates) with my example camera: ca. 150 pixels
#with face rectangle width about 16cm, ear to ear
#Display coordinates:
#Hence 150/16 =9.375 pixel/cm
#z-coordinate 1m is 100cm*9.375 pixel/cm=937.5 pixel.
#hence for face width of w pixels: z-coordinate z= 150/w*937.5 pixels
#Conversion of display coordinates into virtual world coordinates, where 1m in the real world coresponds to 1 in virtual world:
#display coordinates: x,y; virtual world coordinates: xv,yv,zv
#width of head in virtual coordinates: 150/937.5=0.16
#measured width of head in display coordinates: w
#zv=150.0/w
#using prespective projection matrix, which converts the virtual world into display coordinates (here the reverse is necessary):
#xv=x/937.5*zv, yv=y/937.5*zv
#Display size: 480x640 pixel


    print(faces)
    for (x,y,w,h) in faces:
       #face width in display coordinates:

       #center of head in virtual world coordinates, where 1m corresponds to 1,
       #with x=0 and y=0 in the center, positve values go to the right and up
       zv= 150.0/w
       xv=(x-320+w/2)/937.5*zv
       yv=(240-y-h/2)/937.5*zv
       #z-coordinates are negative:
       print("Virtual World Coordinates of center of faces: ", xv,yv,-zv)

    for (x,y,w,h) in faces:
       cv2.rectangle(gray,(x,y),(x+w,y+h),255,2)
       roi_gray = gray[y:y+h, x:x+w]

       eyes = eye_cascade.detectMultiScale(roi_gray)

       for (ex,ey,ew,eh) in eyes:
          cv2.rectangle(gray,(x+ex,y+ey),(x+ex+ew,y+ey+eh),255,2)

    cv2.imshow('Face and Eye Detection',gray)
    #Keep window open until key 'q' is pressed:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
