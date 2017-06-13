#Program to capture a video from a camera and display it live on the screen
#Gerald Schuller, October 2014

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow('Original')
cv2.namedWindow('Luminanz Y')
cv2.namedWindow('Zum Vergleich: Gruen Komponente')
while(True):
    # Capture frame-by-frame
    [ret, frame] = cap.read()

    # Our operations on the frames come here
    #Berechnung der Luminanz-Komponente Y:
    # Y= 0.114*B+0.587*G+0.299*R :
    # /256 because the result is float values which imshow expects in range 0...1:
    Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/256;        
    #Vergleich mit Gruen Komponente:
    G=frame[:,:,1]

    # Display the resulting frame
    cv2.imshow('Original',frame)
    cv2.imshow('Luminanz Y',Y)
    cv2.imshow('Zum Vergleich: Gruen Komponente',G)
    #Ende durch Taste "q":
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
