import numpy as np
import cv2
import sys

#Program to open a video input file in argument and display it on the screen.
#command line example: python videofiledisp.py video.mts
#Gerald Schuller, march 2015

cap = cv2.VideoCapture(str(sys.argv[1]))

while(cap.isOpened()):
    ret, frame = cap.read()


    cv2.imshow('Video',frame)
    #Wait for key for 50ms, to get about 20 frames per second playback 
    #(depends also on speed of the machine, and recording frame rate, try out):
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
