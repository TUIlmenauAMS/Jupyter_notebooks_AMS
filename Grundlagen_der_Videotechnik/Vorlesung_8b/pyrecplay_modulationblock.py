"""
PyAudio Example: Mix speech with a 1 kHz carrier (i.e., record a
few samples, mix/modulate them with a sine wave, and play them back immediately).
Using block-wise processing 
Gerald Schuller, Octtober 2014
"""

import pyaudio
import struct
#import math
#import array
import numpy
#import scipy

CHUNK = 5000 #Blocksize
WIDTH = 2 #2 bytes per sample
CHANNELS = 1 #2
RATE = 32000  #Sampling Rate in Hz
RECORD_SECONDS = 8

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                #input_device_index=10,
                frames_per_buffer=CHUNK)
                

print("* recording")

#Loop for the blocks:
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    #Reading from audio input stream into data with block length "CHUNK":
    data = stream.read(CHUNK)
    #Convert from stream of bytes to a list of short integers (2 bytes here) in "samples":
    #shorts = (struct.unpack( "128h", data ))
    shorts = (struct.unpack( 'h' * CHUNK, data ));
    samples=list(shorts);

    #start block-wise signal processing:

    #Compute a block/an array of sine samples with 500 Hz:
    s=numpy.sin(2*numpy.pi/RATE*500*numpy.arange(0,CHUNK));
    #multiply/modulate the signal with the sine samples:
    samples=samples*s;
    
    #end signal processing

    #converting from short integers to a stream of bytes in "data":
    data=struct.pack('h' * len(samples), *samples);
    #Writing data back to audio output stream: 
    stream.write(data, CHUNK)

print("* done")

stream.stop_stream()
stream.close()

p.terminate()

