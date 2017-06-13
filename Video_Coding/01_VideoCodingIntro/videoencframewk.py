import numpy as np
import cv2
import pickle

#Program to capture video from a camera and store it in an recording file, in Python txt format, using cPickle
#This is a framework for a simple video encoder to build.
#It writes into file 'videorecord.txt'
#Gerald Schuller, April 2015

cap = cv2.VideoCapture(0)

f = open('videorecord.txt', 'w')

#Process 25 frames:
for n in range(25):

    ret, frame = cap.read()

    if ret==True:
        #show captured frame:
        cv2.imshow('frame',frame)

        #Here goes the processing to reduce data...
        reduced = frame.copy()
        reduced = np.array(reduced,dtype='uint8')# for the Cb and Cr components use the int8 type
        #"Serialize" the captured video frame (convert it to a string)
        #using pickle, and write/append it to file f:
        pickle.dump(reduced, f)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        else:
            break

# Release everything if job is finished
cap.release()
f.close()
cv2.destroyAllWindows()
