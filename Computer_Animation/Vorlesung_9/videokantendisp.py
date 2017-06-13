#Program to capture a video from a camera, filter with high pass for edge detection, and display it live on the screen
#Gerald Schuller, October 2014

import numpy as np
import scipy.signal
import cv2

cap = cv2.VideoCapture(0)
[retval, frame] = cap.read()
[r,c,d]=frame.shape
print(r,c)


#High pass filter kernel for edge detection:
filt=np.matrix([[-1.0,-1.0,-1],[-1,8,-1],[-1,-1,-1]])/1.0;
#horizontal edge detector:
#filt=np.matrix([[-1.0,-1.0,-1],[2,2,2],[-1,-1,-1]])/1.0;
#vertical edge detector:
#filt=np.matrix([[-1.0,2.0,-1],[-1.0,2.0,-1],[-1,2,-1]])/1.0;
#Low Pass Kernel:
#filt=np.ones((4,4))/16.0;


while(True):
    # Capture frame-by-frame
    [ret, frame] = cap.read()
    Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/256;
    Yfilt=scipy.signal.convolve2d(Y,filt,mode='same')
    # Display the resulting filtered frame
    cv2.imshow('Y high-pass filtered',np.abs(Yfilt))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
