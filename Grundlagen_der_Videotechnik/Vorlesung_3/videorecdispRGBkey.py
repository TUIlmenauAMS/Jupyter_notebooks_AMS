import numpy as np
import cv2

#Program to capture a video from a camera and display Original and R,G,B, compinents live on the screen, and switch them on and off with the keys r,g,b
#Gerald Schuller, November 2015

cap = cv2.VideoCapture(0)


Ron=True
Gon=True
Bon=True

while(True):
    # Capture frame-by-frame
    [ret, frame] = cap.read()
    cv2.imshow('Original',frame)

    #Null Setzen von Farb-Komponenten:
    if Ron==False:
    #Probeweise nur Farbkomponenten durch setzen von den Y-Komponenten auf einen festen Wert:
      frame[:,:,2]=np.zeros(frame[:,:,2].shape);
    if Gon==False:
      frame[:,:,1]=np.zeros(frame[:,:,1].shape);
    if Bon==False:
      frame[:,:,0]=np.zeros(frame[:,:,0].shape);

   
    #Display resulting video
    #Display text with
    #putText(frame, text string, position, fontFace, fontScale, color, thickness)
    cv2.putText(frame,"Key r: R comp. on/off, R on="+str(Ron), (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
    cv2.putText(frame,"Key g: G comp. on/off, G on="+str(Gon), (20,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
    cv2.putText(frame,"Key b: B comp. on/off, B on="+str(Bon), (20,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
    cv2.imshow('Einzelne Komponenten',frame)

    key=cv2.waitKey(1) & 0xFF;
    if key == ord('r'):     
      Ron= not Ron
    if key == ord('g'):     
      Gon= not Gon
    if key == ord('b'):     
      Bon= not Bon
    if key == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
