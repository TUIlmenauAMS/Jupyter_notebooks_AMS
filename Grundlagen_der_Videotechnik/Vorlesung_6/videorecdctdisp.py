#Program to capture a video from the default camera (0), compute the 2D DCT Type 2
#on the Green component, take the magnitude (phase) and display it live on the screen
#Gerald Schuller, Nov. 2014
import cv2
import numpy as np
import scipy.fftpack as sft

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    [retval, frame] = cap.read()
    #compute magnitude of 2D DCT of green component
    #by applying the DCT first along the rows and the along the columns,
    #with suitable normalization for the display:
    frame=sft.dct(frame[:,:,1]/255.0,axis=1,norm='ortho')
    frame=np.abs(sft.dct(frame,axis=0,norm='ortho'))
    #angle/phase:
    #frame=(3.14+np.angle(np.fft.fft2(frame[:,:,1]/255.0)))/6.28
    # Display the resulting frame
    cv2.imshow('Betrag der 2D - DCT Typ 2 des Videos',frame)
    #Keep window open until key 'q' is pressed:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
