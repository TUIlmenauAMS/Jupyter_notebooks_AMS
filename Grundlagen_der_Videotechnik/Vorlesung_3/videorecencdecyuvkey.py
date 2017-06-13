#Program to capture a video from a camera, transform it to YUV, transform it back, and display it live on the screen
#Gerald Schuller,November 2015

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

Yon=True
Uon=True
Von=True

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
    # Y= 0.114*B+0.587*G+0.299*R :
    # /256 because the result is float values which imshow expects in range 0...1:
    Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/255;        
    #U=B-Y:
    U=frame[:,:,0]/255.0-Y;
    #V=R-Y:
    V=frame[:,:,2]/255.0-Y;

    ####################Decoder ################ 
    
    #Inverse Farb-Transformation im Decoder:

    if Yon==False:
      #Probeweise nur Farbkomponenten durch setzen von den Y-Komponenten auf einen festen Wert:
      Y=np.ones(Y.shape)*0.5;
    #Probeweise Null setzen von Farb-Komponenten:
    if Uon==False:
      U=np.zeros(U.shape);
    if Von==False:
      V=np.zeros(V.shape);

    B=U+Y
    R=V+Y
    G=(Y-0.114*B-0.299*R)/0.587;
    #Schreibe die RGB Komponenten in den rekonstruierten Frame: 
    framerec[:,:,0]=B;
    framerec[:,:,1]=G;
    framerec[:,:,2]=R;

    #Display reconstructed video
    #Display text with
    #putText(frame, text string, position, fontFace, fontScale, color, thickness)
    cv2.putText(framerec,"Key y: Y comp. on/off, Y on="+str(Yon), (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),2)
    cv2.putText(framerec,"Key u: U comp. on/off, U on="+str(Uon), (20,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
    cv2.putText(framerec,"Key v: V comp. on/off, V on="+str(Von), (20,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

    cv2.imshow('Reconstructed, exit with q',framerec)    
    
    key=cv2.waitKey(1) & 0xFF;
    if key == ord('y'):     
      Yon= not Yon
    if key == ord('u'):     
      Uon= not Uon
    if key == ord('v'):     
      Von= not Von
    #Ende durch Taste "q":
    if key == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
