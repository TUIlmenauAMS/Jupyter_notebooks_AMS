#Program to capture a video from a camera and display it live on the screen
#Gerald Schuller, October 2014

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow('Original')
cv2.namedWindow('Luminanz Y')
cv2.namedWindow('Farbkomponente U')
cv2.namedWindow('Farbkomponente V')
while(True):
    # Capture frame-by-frame
    [ret, frame] = cap.read()

    # Our operations on the frames come here
    #Berechnung der Luminanz-Komponente Y:
    # Y= 0.114*B+0.587*G+0.299*R :
    # /256 because the result is float values which imshow expects in range 0...1:
    Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/255;        
    #U=B-Y:
    U=frame[:,:,0]/255.0-Y;
    #V=R-Y:
    V=frame[:,:,2]/255.0-Y;

    # Display the resulting frame
    cv2.imshow('Original',frame)
    cv2.imshow('Luminanz Y',Y)
    cv2.imshow('Farbkomponente U',np.abs(U))
    cv2.imshow('Farbkomponente V',np.abs(V))
    #Ende durch Taste "q":
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
