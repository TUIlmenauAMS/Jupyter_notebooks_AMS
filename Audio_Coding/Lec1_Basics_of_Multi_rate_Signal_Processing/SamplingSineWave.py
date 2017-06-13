import numpy as np
from sound import *
import matplotlib.pyplot as plt

fs = 44100
f = 400
s = np.sin(2 * np.pi * f *np.arange(0, 1., 1./fs))

#Listen to it:
sound(s*2**15, fs)

#Now plot the first 1000 samples:
plt.plot(s[:1000])
plt.show()

#Now plot the first 1000 samples:
plt.plot(s[:100])
plt.show()

#Now we can multiply this sine tone signal with a unit pulse train, with N=8.
#We use an indexing trick to get the desired result of only keeping every 8th sample and having zeros in between:
sdu = np.zeros(s.shape)
sdu[::8] = s[::8]

#Now plot the result, the first 100 samples:
plt.plot(sdu[:100])
plt.show()

#Now take a look at the spectrum of the original signal s:
from freqz import *
freqz(s, axisFreqz=[0, np.pi, -50, 60])

#Now we can compare this to our signal with the zeros, sdu:
freqz(sdu, axisFreqz=[0, np.pi, -50, 60])

#Now also listen to the signal with the zeros:
sound(sdu*2**15, 44100)

sd = np.zeros(sdu.shape[0]/8)
sd = sdu[::8]
plt.plot(sd[:100/8])
plt.show()
