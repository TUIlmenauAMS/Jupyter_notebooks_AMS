import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np

rate, snd = wav.read('sndfile.wav')
#Take an excerpt of 1000 samples, 
#starting at sample 2001 and plot it:
spex = snd[2000 + np.arange(1, 1000)]
plt.plot(spex)
plt.show()

plt.plot(spex[2::2], spex[1::2], '+')
plt.show()
