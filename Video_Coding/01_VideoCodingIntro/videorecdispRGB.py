import numpy as np
import cv2

#Program to capture a video from a camera and display Original and R,G,B, components live on the screen

cap = cv2.VideoCapture(0)

cv2.namedWindow('Original')
cv2.namedWindow('B Komponente')
cv2.namedWindow('G Komponente')
cv2.namedWindow('R Komponente')

while(True):
    # Capture frame-by-frame
    [ret, frame] = cap.read()

    # Display the resulting frame
    cv2.imshow('Original',frame)
    cv2.imshow('B Komponente',frame[:,:,0])
    cv2.imshow('G Komponente',frame[:,:,1])
    cv2.imshow('R Komponente',frame[:,:,2])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
