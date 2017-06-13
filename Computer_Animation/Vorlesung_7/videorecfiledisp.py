import numpy as np
import cv
import cv2

#Program to capture a video from a camera display it live on the screen, and write it to a file
#Gerald Schuller, Dec 2014

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
height , width , layers =  frame.shape
# Define the codec and create VideoWriter object
#fourcc = cv.CV_FOURCC(*'XVID')
fourcc = cv.CV_FOURCC('D','I','V','X')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#Open video output file:
out = cv2.VideoWriter('videorec.avi',fourcc, 20.0, (width,height))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #cv2.imshow('frame',gray)
    cv2.imshow('Video',frame)

    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
