import cv2

#Progeam to capture a video from the default camera(0) and display it live on the screen
cap = cv2.VideoCapture(0)

while(True):
    #capture frame-by-frame
    retval, frame = cap.read()
    
    #Display the resulting frame
    cv2.imshow()
    
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break
        
#when everything done, release the capture
cap.release()
cv2.destroyAllWindows()