a=0.5;
B=[1/a.conjugate()]; #the numerator polynomial of H_AP
A=[a]; #the denominator polynomial

from zplane import zplane
zplane(B,A,[-1.1, 2.1, -1.1, 1.1]); #plot the pole/zero diagram with axis limits

import numpy as np
def warpingphase(w, a):
    #produces (outputs) phase wy for an allpass filter
    #w: input vector of normlized frequencies (0..pi)
    #a: allpass coefficient
    #phase of allpass zero/pole :
    theta = np.angle(a);
    #magnitude of allpass zero/pole :
    r = np.abs(a);
    wy = -w-2*np.arctan((r*np.sin(w-theta))/(1-r*np.cos(w-theta)))
    return wy
	
import matplotlib.pyplot as plt
#from warpingphase import *
#frequency range:
w = np.arange(0,np.pi, 0.01)
a = 0.5 * (1+1j)
wyy = (warpingphase(warpingphase(w,a),-a.conjugate()))
plt.plot(w,wyy)
plt.xlabel('Normalized Frequency')
plt.ylabel('Phase Angle')
plt.show()
a=0.5;
B=[-a.conjugate(), 1]
A=[1, -a]

from freqz import freqz
freqz(B,A)

from scipy import signal as sp
Imp = np.zeros(21)
Imp[0] = 1
h = sp.lfilter(B, A, Imp)
plt.plot(h)
plt.show()

print h[0:4]