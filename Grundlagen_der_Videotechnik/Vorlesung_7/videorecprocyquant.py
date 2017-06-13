#Program to capture a video from a camera, compute the Y component, quantize and de-quantize itm and display it live on the screen
#Gerald Schuller, October 2014

import numpy as np
import cv2

#Number of bits per Y pixel
bits=2
#resulting quantization step size for 2^bits steps, with min=0 and max=1:
quantstufe=1.0/(2**bits-1)

cap = cv2.VideoCapture(0)

#cv2.namedWindow('Original Y')
#cv2.namedWindow('De-Quantisierte Luminanz Y')

while(True):
    # Capture frame-by-frame
    [ret, frame] = cap.read()

    # Our operations on the frames come here
    #Berechnung der Luminanz-Komponente Y:
    # Y= 0.114*B+0.587*G+0.299*R :
    # /256 because the result is float values which imshow expects in range 0...1:
    Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/255;        
   
    #Quantization indices for transmission:
    indices=np.round(Y/quantstufe)
    #de-quantization in the decoder:
    Yrek=indices*quantstufe

    # Display the resulting frame
    cv2.imshow('Original Y, 8 bits/Pixel',Y)
    cv2.imshow('De-Quantisierte Luminanz Y, 2 bits/Pixel',Yrek)

    #Ende durch Taste "q":
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
