import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

from sound import *
x,fs=wavread('speech8kHz.wav')
np.shape(x)

x = np.matrix(x,dtype=float).T / 2 ** 15

sound(np.array(x.T)[0] * 2 ** 15, fs)

A = np.matrix(np.zeros((60000,10)));
for m in range(0,60000):
    A[m, :] = x[m + np.arange(10)].T
	
d = x[np.arange(10, 60010)]

h = np.linalg.inv(A.T*A) * A.T * d
np.flipud(h)

plt.plot(np.flipud(h))
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('Impulse Response of our Prediction Filter')
plt.show()

hpred = np.vstack([0, np.flipud(h)])

xpred = sp.lfilter(np.array(hpred.T)[0], 1, np.array(x.T)[0])

plt.plot(x);
plt.plot(xpred,'red')
plt.legend(('Original','Predicted'))
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('Our Speech Wave Form')
plt.show()

hperr = np.vstack([1, -np.flipud(h)])

e = sp.lfilter(np.array(hperr.T)[0], 1, np.array(x.T)[0])

e = np.matrix(e)

e * e.T / np.max(np.shape(e))

x.T * x/np.max(np.shape(x))

sound(2 ** 15 * np.array(e)[0],fs)

plt.plot(2**15*x)
plt.plot(2**15*e.T,'r')
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('Our Speech and Prediction Error Wave Forms')
plt.legend(('Original', 'Prediction Error'))
plt.show()

#decoder

xrec = sp.lfilter([1], np.array(hperr.T)[0], np.array(e)[0])
plt.plot(x)
plt.plot(xrec,'r')
plt.show()

