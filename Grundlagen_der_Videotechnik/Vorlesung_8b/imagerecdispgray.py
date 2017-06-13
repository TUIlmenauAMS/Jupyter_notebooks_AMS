#Program to capture an image from a camera display a monochrome version of it on the screen,
#and store it in the file 'pygrayphoto.jpg'.
#Gerald Schuller, Sep. 2014.


import numpy as np
import cv2
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)


 # Capture frame-by-frame
ret, frame = cap.read()

# Our operations on the frame come here
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Display the resulting frame
cv2.imshow('frame',gray)
#cv2.imshow('frame',frame)
#plt.imshow(gray,cmap='gray');
#plt.imshow(frame);
cv2.imwrite('pygrayphoto.jpg', gray)


while(True):
   if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
