import numpy as np
import cv2
import sys
import cPickle as pickle

#Program to open a video input file 'videorecord.txt' (python txt format using pickle) and display it on the screen.
#This is a framework for a simple video decoder to build.
#Gerald Schuller, April 2015

f = open('videorecord.txt', 'r')


try:
    while True:
    #load next frame from file f and "de-pickle" it, convert from a string back to matrix or tensor:
        reduced = pickle.load(f)

        #here goes the decoding:
        framedec = reduced.copy()

        cv2.imshow('Video', framedec)
        #Wait for key for 50ms, to get about 20 frames per second playback
        #(depends also on speed of the machine, and recording frame rate, try out):
        if cv2.waitKey(500) & 0xFF == ord('q'):
            break
except (EOFError):
    pass


# cap.release()
cv2.destroyAllWindows()
