from sound import *
import scipy.signal
x, fs = wavread('speech8kHz.wav')

sound(x,fs)

#FIR low pass filter
h = [0.5, 1, 1.1, 0.6]

#polyphase representation for filter and the signal resp.
h0 = h[0::2]
h1 = h[1::2]

x0 = x[0::2]
x1 = x[1::2]

#Apply filter using polyphase representation
y = scipy.signal.lfilter(h0,1,x0)+scipy.signal.lfilter(h1,1,x1)

sound(y,fs/2)

#Using Noble Identies
import scipy.signal
import numpy as np
from sound import *

h = np.array([0.5, 1, 1, 0.5])

h0 = h[0::2]
h1 = h[1::2]

y0 = scipy.signal.lfilter(h0,1,y)
y1 = scipy.signal.lfilter(h1,1,y)

L = np.max([len(y0), len(y1)])
yu = np.zeros(2*L)
yu[0::2] = y0
yu[1::2] = y1

sound(yu/2,fs)