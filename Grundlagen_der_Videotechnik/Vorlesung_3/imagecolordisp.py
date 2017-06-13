import numpy as np
import cv2
import matplotlib.pyplot as plt

#Program to display all possible display colors on the screen in a color triangle

#make frames of 300x300 pixels with 3 equal color components:
frame=np.zeros((300,300,3))
frame[:,:,0]=np.ones((300,300))*0.8
frame[:,:,1]=np.ones((300,300))*0.6
frame[:,:,2]=np.ones((300,300))*0.2

frame=frame*1.0;

# Display the resulting frame
cv2.imshow('frame',frame)

while(True):
   if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, close windows

cv2.destroyAllWindows()
