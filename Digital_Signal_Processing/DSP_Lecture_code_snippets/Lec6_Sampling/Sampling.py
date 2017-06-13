import numpy as np
import matplotlib.pyplot as plt
fs = 44100
f = 400.0
s = np.sin(2*np.pi*f*np.arange(0, 1, 1.0/fs))

from sound import sound
sound((2**15)*s,fs)

#Now plot the first 1000 samples
plt.plot(s[0:1000])
plt.show()

#Next plot the first 100 samples
plt.plot(s[0:100])
plt.show()

#We generate the unit impulse train
unit = np.zeros(44100)
unit[0::8] = 1

plt.plot(unit[0:100])
plt.xlabel('n')
plt.ylabel('unit(n)')
plt.show()


#Listen to it, with scaling to the value range for 16 bit/sample
sound(unit*2.0**15,44100)

#The multiplication with the unit impulse train
sdu=s*unit

Now plot the result, the first 100 samples:
In [9]:

#Now plot the result, the first 100 samples
plt.plot(sdu[0:100])
plt.show()

#This is our signal still with the zeros in it. Now take a look at the magnitude spectrum (in dB) of the original signal s
from scipy.signal import freqz
w, h = freqz(s)
plt.plot(w, 20*np.log10(np.abs(h) + 1e-3)) #Adding 1e-3 to avoid log(0)
plt.xlabel('Frequency')
plt.ylabel('dB')
plt.title('Magnitude Frequency Response')
plt.show()

#Now we can compare this to our signal with the zeros, sdu
ws, hs = freqz(sdu) #ws, hs are normalized frequency and magnitude for sampled signal
plt.plot(w, 20*np.log10(np.abs(h) + 1e-3)) 
plt.plot(ws, 20*np.log10(np.abs(hs) + 1e-3))
plt.legend(('Original Sinusoid', 'Sampled Sinusoid'))
plt.show()

#Now also listen to the signal with the zeros
sound(sdu*2.0**15,44100)

#Removing the zeros
#Taking every 8th sample which in our case are the only non-zero values
sd = sdu[0:44100:8]
plt.plot(sd[0:100/8])
plt.show()

#We can now take a look at the spectrum with
wd, hd = freqz(sd)
plt.plot(wd, 20*np.log10(np.abs(hd) + 1e-3))
plt.xlabel('Frequency')
plt.ylabel('dB')
plt.title('Magnitude Frequency Response')
plt.show()

