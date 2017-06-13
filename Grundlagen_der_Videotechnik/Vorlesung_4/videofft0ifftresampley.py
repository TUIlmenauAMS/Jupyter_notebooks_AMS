#Program to capture a video from a camera, compute the Y-component, 
#downsample it by a factor of N horizontally and vertically, and display 
#it live on the screen
#Gerald Schuller, Nov. 2014

import numpy as np
import cv2
#import scipy.signal

cap = cv2.VideoCapture(0)

#cv2.namedWindow('Original')
#cv2.namedWindow('Luminanz Y')
#cv2.namedWindow('Unterabgetastetes Y')

#Low Pass Kernel:
#filt=np.ones((8,8))/16.0;

#Downsampling factor N:
N=4;
[ret, frame] = cap.read()
[rows,cols,c]=frame.shape;
r=rows
c=cols
Ds0=np.zeros((rows,cols));
Ds=Ds0

#Mask to set to zero the 7/8 highest frequencies, 
#only kep the 1/8 lowest frequencies in each direction:
#For rows:
Mr=np.ones((r,1)) 
Mr[(r/8.0):(r-r/8.0),0]=np.zeros((3.0/4.0*r))
#For columns:
Mc=np.ones((1,c)) 
Mc[0,(c/8.0):(c-c/8)]=np.zeros((3.0/4.0*c));
#Together:
M=np.dot(Mr,Mc)


while(True):
    #Encoding side:
    # Capture frame-by-frame
    [ret, frame] = cap.read()

    #Berechnung der Luminanz-Komponente Y:
    # Y= 0.114*B+0.587*G+0.299*R :
    # /256 because the result is float values which imshow expects in range 0...1:
    Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/256;   
    #Downgesamplets Y, nur jedes Nte pixel horizontal und vertikal wir uebertragen:
    #Ds[0::N,::N]=Y[0::N,::N];  
    #2D-FFT of Y 
    X=np.fft.fft2(Y)
    #Set to zero the 7/8 highest spacial frequencies in each direction:
    X=X*M   
    #inverse 2D-FFT:
    Y0=np.abs(np.fft.ifft2(X))
    #Downgesamplets Y0, nur jedes Nte pixel horizontal und vertikal wir uebertragen:
    Ds0[0::N,::N]=Y0[0::N,::N];

    #Decoding Side
    #Lowpass filter the sampled frame:
    #Dsfilt=N*scipy.signal.convolve2d(Ds0,filt,mode='same')
    Ds0fft=np.fft.fft2(Ds0)
    #Set to zero the 7/8 highest spacial frequencies in each direction:
    Ds1fft=Ds0fft*M   
    #inverse 2D-FFT:
    Yrek=np.abs(np.fft.ifft2(Ds1fft))

    # Display the resulting frames
    
    #cv2.imshow('Downgesampletes Y',Ds)
    cv2.imshow('Decoder: Gefilterte Sampled Frames',Yrek*N*N)
    cv2.imshow('Decoder: FFT Bereich nach Null Setzen',np.abs(Ds1fft)/100)
    cv2.imshow('Decoder: FFT Bereich der Sampled Frames ',np.abs(Ds0fft)/100)
    cv2.imshow('Encoder: Sampled Frames',Ds0)
    cv2.imshow('Encoder: Video nach Nullsetzen der hohen Ortsfrequenzen',Y0)
    cv2.imshow('Encoder 2D FFT von Y und Null Setzen',np.abs(X)/(480))
    #cv2.imshow('Original',frame)
    cv2.imshow('Encoder: Luminanz Y',Y)
    
    
    
    
    #Ende durch Taste "q":
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
