#Program to capture a video from the default camera (0), compute the 2D FFT 
#on the Green component, take the magnitude (phase) and display it live on the screen
#Gerald Schuller, Nov. 2014
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#Get size of frame:
[retval, frame] = cap.read()
[r,c,d]=frame.shape
print(r,c)

#Mask to set to zero the 3/4 highest frequencies, 
#only kep the 1/4 lowest frequencies in each direction:

#For rows:
Mr=np.ones((r,1)) 
Mr[(r/8.0):(r-r/8.0),0]=np.zeros((3.0/4.0*r))
#For columns:
Mc=np.ones((1,c)) 
Mc[0,(c/8.0):(c-c/8)]=np.zeros((3.0/4.0*c));
#Together:
M=np.dot(Mr,Mc)

while(True):
    # Capture frame-by-frame
    [retval, frame] = cap.read()    
    cv2.imshow('Original Video, Gruen Komponente',frame[:,:,1])

    #compute magnitude of 2D FFT of green component 
    #with suitable normalization for the display:
    X=np.fft.fft2(frame[:,:,1]/255.0)
    #Set to zero the 7/8 highest spacial frequencies in each direction:
    X=X*M
    frame=np.abs(X)/512.0
    #angle/phase:
    #frame=(3.14+np.angle(np.fft.fft2(frame[:,:,1]/255.0)))/6.28
    # Display the resulting frame
    cv2.imshow('2D-FFT mit Null Setzen der hoechsten Ortsfrequenzen',frame)
    #Inverse FFT, with abs to turn complex into float numbers:
    x=np.abs(np.fft.ifft2(X))
    cv2.imshow('Inverse 2D FFT ohne die hoechsten Ortsfrequenzen', x)
    
    #Keep window open until key 'q' is pressed:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
