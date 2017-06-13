#Program to capture a video from a camera, filter is, and display it live on the screen
#Gerald Schuller, October 2014

import numpy as np
import scipy.signal
import cv2

cap = cv2.VideoCapture(0)
[retval, frame] = cap.read()
[r,c,d]=frame.shape
print(r,c)
#2D-Mask to set to zero the 7/8 highest frequencies, 
#only kep the 1/8 lowest frequencies in each direction:
#For rows:
Mr=np.ones((r,1)) 
Mr[(r/8.0):(r-r/8.0),0]=np.zeros((3.0/4.0*r))
#For columns:
Mc=np.ones((1,c)) 
Mc[0,(c/8.0):(c-c/8)]=np.zeros((3.0/4.0*c));
#Together:
M=np.dot(Mr,Mc)
#Conmpute space-domain/inverse 2D Fourier transform of Low Pass filter:
h=np.abs(np.fft.ifft2(M))
hc=np.concatenate((h[:,(c/2):c],h[:,0:(c/2)]),axis=1)
hc=np.concatenate((hc[(r/2):r,:],hc[0:(r/2),:]))
#Only keep the piece with the biggest components:
hc=hc[(r/2-10):(r/2+10),(c/2-10):(c/2+10)]
filt=hc

#High pass filter kernel for edge detection:
#filt=np.matrix([[-1.0,-1.0,-1],[-1,8,-1],[-1,-1,-1]])/1.0;
#Low Pass Kernel:
#filt=np.ones((4,4))/16.0;


while(True):
    # Capture frame-by-frame
    [ret, frame] = cap.read()
    Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/256; 
    Yfilt=scipy.signal.convolve2d(Y,filt,mode='same')
    # Display the resulting filtered frame
    cv2.imshow('Y low-pass filtered',Yfilt)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
