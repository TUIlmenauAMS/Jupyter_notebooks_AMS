#Program to capture an image from a camera and display it on the screen
#Gerald SChuller, October 2014

import cv2

cap = cv2.VideoCapture(0)

 # Capture frame
[ret, frame] = cap.read()

# Display the resulting frame
cv2.imshow('Photo',frame)
#write photo to jpg file:
cv2.imwrite('pycolorphoto.jpg', frame)

#Keep photo window open until key 'q' is pressed:
while(True):
   if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
