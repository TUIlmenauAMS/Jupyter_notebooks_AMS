import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy.signal as sig
from optimfuncQMF import optimfuncQMF

#optimize for 16 filter coefficients:
xmin = opt.minimize(optimfuncQMF, 16*np.ones(16), method='SLSQP')
xmin = xmin["x"]

#Restore symmetric upper half of window:
h = np.concatenate((xmin, np.flipud(xmin)))
plt.plot(h)
plt.title('Resulting PQMF Window Function')
plt.xlabel('Sample')
plt.ylabel('Value')
plt.show()

f, H = sig.freqz(h)
plt.plot(f, 20*np.log10(np.abs(H)))
plt.title('Resulting PQMF Magnitude Response')
plt.xlabel('Normalized Frequency')
plt.ylabel('dB')
plt.show()

#Unity condition check
N = 4
f, H_im = sig.freqz(h)
posfreq = np.square(H[0:512/N])
negfreq = np.flipud(np.square(H[0:512/N]))
plt.plot((np.abs(posfreq) + np.abs(negfreq)))
plt.xlabel('Frequency (512 is Nyquist)')
plt.ylabel('Magnitude')
plt.title('Unity Condition, Sum of Squared Magnitude of 2 Neighboring Subbands')
plt.show()