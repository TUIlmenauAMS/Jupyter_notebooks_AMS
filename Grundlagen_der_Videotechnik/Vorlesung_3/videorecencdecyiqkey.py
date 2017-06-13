#Program to capture a video from a camera, transform it to YIQ, transform it back, and display it live on the screen
#Gerald Schuller, November 2015

import numpy as np
import cv2
from numpy.linalg import inv

cap = cv2.VideoCapture(0)

#YIQ transform matrix:
T=np.array([[0.299, 0.587, 0.114],
[0.595, -0.274, -0.321],
[0.211,-0.522, 0.311]])

#inverse color transform:
#Inverse matrix as array:
#Tinv=np.array(np.matrix(T).I)
Tinv=inv(T)



Yon=True
Ion=True
Qon=True

while(True):
    # Capture frame-by-frame
    [ret, frame] = cap.read()
    framerec=np.zeros(frame.shape);

    # Display the original frame
    cv2.imshow('Original',frame)

    # Our operations on the frames come here
    ######Encoder###########################
    #Forwaerts Farb-Transformation im Encoder:
    #Berechnung der Luminanz-Komponente Y und der Farb-Komponenten U und V:
    # /256 because the result is float values which imshow expects in range 0...1:
    #np.dot applies the matrix multiplication to the last axis, hence here the RGB axis:
    YIQ= np.dot(frame,T)/255.0
    #Result is 3-dimensional matrix, rows x columns x color components


    ####################Decoder ################ 
    
    #Inverse Farb-Transformation im Decoder:

    if Yon==False:
      #Probeweise nur Farbkomponenten durch setzen von den Y-Komponenten auf einen festen Wert:
      YIQ[:,:,0]=np.ones(YIQ[:,:,0].shape)*0.5;
    #Probeweise Null setzen von Farb-Komponenten:
    if Ion==False:
      YIQ[:,:,1]=np.zeros(YIQ[:,:,1].shape);
    if Qon==False:
      YIQ[:,:,2]=np.zeros(YIQ[:,:,2].shape);

    #Inverse color transform: 
    #np.dot applies the matrix multiplication to the last axis, hence here the color axis:
    framerec=np.dot(YIQ,Tinv)
    
    
    #Display reconstructed video
    #Display text with
    #putText(frame, text string, position, fontFace, fontScale, color, thickness)
    cv2.putText(framerec,"Key y: Y comp. on/off, Y on="+str(Yon), (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),2)
    cv2.putText(framerec,"Key i: I comp. on/off, I on="+str(Ion), (20,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
    cv2.putText(framerec,"Key q: Q comp. on/off, Q on="+str(Qon), (20,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

    cv2.imshow('Reconstructed, exit with x',framerec)    
    
    key=cv2.waitKey(1) & 0xFF;
    if key == ord('y'):     
      Yon= not Yon
    if key == ord('i'):     
      Ion= not Ion
    if key == ord('q'):     
      Qon= not Qon
    #Ende durch Taste "x":
    if key == ord('x'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
