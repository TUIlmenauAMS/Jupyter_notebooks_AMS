from sound import *
from scipy import signal as sp
import numpy as np
import matplotlib.pyplot as plt

x, fs = wavread('speech8kHz.wav')

x = np.matrix(x).T

sound(np.array(x), fs)

y = x + 0.1 * (np.random.random(np.shape(x)) - 0.5) * 2 ** 15

sound(np.array(y), fs)

A = np.matrix(np.zeros((60230, 10)))

for m in range(60230):
    A[m,:] = y[m+np.arange(10)].T
print A.shape

h = np.linalg.inv(A.T*A)*A.T*x[5:60235]
plt.plot(np.flipud(h))
plt.xlabel('Sample')
plt.ylabel('value')
plt.title('Impulse Response of Wiener Filter')
plt.show()

from freqz import *
freqz(np.flipud(h))

w, Hspeech = sp.freqz(x);
w, Hnoise = sp.freqz(0.1*(np.random.random(np.shape(x)) - 0.5) * 2 ** 15)
w, Hw = sp.freqz(np.flipud(h))

plt.plot(w, 20 * np.log10(np.abs(Hspeech)))
plt.hold
plt.plot(w, 20 * np.log10(np.abs(Hnoise)),'r')
#plot and shift the filter into the vicinity of the signal:
plt.plot(w, 20 * np.log10(np.abs(Hw)) + 100,'g');
plt.xlabel('Normalized Frequency')
plt.ylabel('Magnitude (dB)')
plt.legend(('Speech', 'White Noise', 'Wiener Filter'))
plt.title('Magnitude Spectrum')
plt.show()

xw = sp.lfilter(np.array(np.flipud(h).T)[0], [1], np.array(y.T)[0])

sound(xw, fs)

print np.shape(x)

np.sum(np.power(y[:50000]-x[:50000],2))/50000

np.sum(np.power(xw[4:50004] - x[:50000].T,2))/50000