import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

h = np.zeros(20);
n = np.arange(-9, 10, 2);
h[n + 10] = 2/(np.pi * n)
plt.stem(np.arange(-10, 10), h)
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('Part of Imp. Resp. of Hilbert Transform')
plt.show()

from freqz import freqz
freqz(h, axisFreqz = [0, np.pi, -50, 10], axisPhase=[0, np.pi, -np.pi, np.pi])

# construct a delayed impulse to implement the
# delay for the real part:
delt = np.zeros(20)
delt[9] = 1

#Then we need to add our imaginary part as our
#Hilbert transform to obtain our complex filter:
h = np.zeros(20);
n = np.arange(-9, 10+1, 2);
h[(n-1)+10] = 2./(np.pi*n);
hone = delt+h*1j


freqz(hone,1, whole=True, axisFreqz=[0,2*np.pi,-40,10])

b=sp.remez(21, [0.03, 0.47], [1], type='hilbert')
freqz(b, axisPhase = [0, np.pi, -np.pi, np.pi])

#Delay for the real part:
delt = np.zeros(21)
delt[10] = 1
#The complex filter:
honeremez = delt + 1j*b.conjugate()


freqz(hone,1, whole=True, axisFreqz=[0, 6.28,-40,10])

import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

x = 2 * np.sin(np.pi * 0.05 * np.arange(0, 40))
plt.plot(x)
plt.show()

xhone = sp.convolve(x, hone)
plt.plot(np.real(xhone))
plt.plot(np.imag(xhone),'r')
plt.show()

plt.plot(np.abs(xhone))
plt.show()
