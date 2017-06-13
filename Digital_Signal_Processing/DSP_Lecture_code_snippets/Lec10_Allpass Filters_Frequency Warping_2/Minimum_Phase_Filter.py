import numpy as np
import matplotlib.pyplot as plt

hsinc = np.sinc(np.linspace(-2,2,11))
print hsinc

plt.plot(hsinc)
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('Piece of Sinc Function')
plt.show()

from zplane import *
hsinc = np.sinc(np.linspace(-2, 2, 11))
zplane(np.roots(hsinc), 0, [-1.1, 2.1, -1.1, 1.1])

abs(np.roots(hsinc))

rt = np.roots(hsinc)

import scipy.signal as sp
[b, r] = sp.deconvolve(hsinc, [1,-rt[1]])	

hsincmp = sp.convolve(b,[1,-1/rt[1].conjugate()])
hsincmp

#impulse response
plt.plot(hsincmp)
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('Impulse Response of the Minimum Phase Filter')
plt.show()

from freqz import *
freqz(hsincmp)

freqz(hsinc)