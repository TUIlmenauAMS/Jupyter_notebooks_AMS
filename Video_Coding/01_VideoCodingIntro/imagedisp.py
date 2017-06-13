#Program to display an image from a file given in the argument and display it on the screen
#example command line: python imagedisp.py picture.jpg
#Gerald Schuller, March 2015

import cv2
import sys

photo=cv2.imread(str(sys.argv[1]));
# Display the resulting frame
cv2.imshow('Photo',photo)

#Keep photo window open until key 'q' is pressed:
while(True):
   if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
