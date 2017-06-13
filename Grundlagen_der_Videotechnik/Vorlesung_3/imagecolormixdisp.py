import numpy as np
import cv2
import matplotlib.pyplot as plt

#Program to display colors and color mix on the screen

#cv2.namedWindow('Farbe1')
#cv2.namedWindow('Farbe2')
#cv2.namedWindow('Mischfarbe')

#make frames of 300x300 pixels with 3 equal color components:
Farbe1=np.ones((300,300,3))
Farbe1[:,:,0]=np.ones((300,300))*0.6
Farbe1[:,:,1]=np.ones((300,300))*0.4
Farbe1[:,:,2]=np.ones((300,300))*0.1

Farbe2=np.ones((300,300,3))
Farbe2[:,:,0]=np.ones((300,300))*0.3
Farbe2[:,:,1]=np.ones((300,300))*0.6
Farbe2[:,:,2]=np.ones((300,300))*0.1

#This is the color mixing:
Mischfarbe=0.2*Farbe1+0.8*Farbe2

# Display the resulting frame
cv2.imshow('Farbe1',Farbe1)
cv2.imshow('Farbe2',Farbe2)
cv2.imshow('Mischfarbe',Mischfarbe)

while(True):
   if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, close windows

cv2.destroyAllWindows()
