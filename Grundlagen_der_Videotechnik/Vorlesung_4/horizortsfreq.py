#Program to generate a horizontal spatial frequency, store it in a file, and display it on the screen
#Gerald SChuller, Nov 2014

import cv2
import numpy as np

#1000 sine values between 0 and 2pi*f for f periods over the width of the 
#picture, add a 1.0 to get all positive numbers, divide by 2 to get the 
#normalized range between 0 and 1, which imwrite expects for floats:
f=100;
sinewave=(1.0+np.sin(np.linspace(0,2*np.pi*f,1000)))/2
#Diagonal matrix with sine wave on the diagonal:
d=np.diag(sinewave)
#Matrix with sinewave from left to right, identically on each row, with 500 rows:
A=np.dot(np.ones((500,1000)),d)

# Display the resulting frame
cv2.imshow('Horizontale Ortsfrequenz',A)
#write photo to jpg file. Mult with 255 because imwrite expects a range of 0...255:
cv2.imwrite('horizOrtsfreq.jpg', 255*A)

#Keep photo window open until key 'q' is pressed:
while(True):
   if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cv2.destroyAllWindows()
