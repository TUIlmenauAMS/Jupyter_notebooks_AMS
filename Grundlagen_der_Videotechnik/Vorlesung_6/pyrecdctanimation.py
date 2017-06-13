"""
Using Pyaudio, record sound from the audio device and plot the dct magnitude spectrum life, for 8 seconds.
Usage example: python pyrecdctanimation.py
Gerald Schuller, November 2014
"""

import pyaudio
import struct
#import math
#import array
import numpy as np
import scipy.fftpack
#import sys
#import wave
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import pylab
#import cv2

CHUNK = 2048 #Blocksize
WIDTH = 2 #2 bytes per sample
CHANNELS = 1 #2
RATE = 32000  #Sampling Rate in Hz
RECORD_SECONDS = 70

dctlen=CHUNK/2;

[fig, ax] = plt.subplots()
plt.ylabel('dB')
plt.xlabel('DCT Type 2 bins/Subbands')
plt.title('Live DCT Type 2 Magnitude Spectrum of Microphone Signal')

x = np.arange(0, dctlen)        # x-array
#Set scale on y-axis and generate line object with it:
[line, ]= ax.plot(x, 100.0**np.sin(x))

def animate(i):
    # update the data
    #Reading from audio input stream into data with block length "CHUNK":
    data = stream.read(CHUNK)
    #Convert from stream of bytes to a list of short integers (2 bytes here) in "samples":
    #shorts = (struct.unpack( "128h", data ))
    shorts = (struct.unpack( 'h' * CHUNK, data ));
    samples=np.array(list(shorts),dtype=float);

    #plt.plot(samples)  #<-- here goes the signal processing.
    line.set_ydata(20.0*np.log10((np.abs(scipy.fftpack.dct(samples[0:dctlen])/np.sqrt(dctlen))+1)))
    #line.set_ydata(samples)
    return line,

def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,


p = pyaudio.PyAudio()

a = p.get_device_count()
print("device count=",a)

for i in range(0, a):
    print("i = ",i)
    b = p.get_device_info_by_index(i)['maxInputChannels']
    print(b)
    b = p.get_device_info_by_index(i)['defaultSampleRate']
    print(b)

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                #input_device_index=3,
                frames_per_buffer=CHUNK)


print("* recording")

#ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
#    interval=25, blit=True)
ani = animation.FuncAnimation(fig, animate,  init_func=init, interval=25, blit=True)
plt.show()


# When everything done, release the capture

print("* done")

f.close()
stream.stop_stream()
stream.close()
