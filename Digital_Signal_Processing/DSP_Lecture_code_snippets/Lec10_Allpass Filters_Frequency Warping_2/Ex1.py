# First as a comparison: design an unwarped filter with 4 coefficients/taps with these specifications:

import scipy.signal as sp
cunw = sp.remez(4, [0, 0.025, 0.025+0.025, 0.5], [1,0], [1, 100])
print 'cunw = ', cunw

#impulse response:
import matplotlib.pyplot as plt
plt.plot(cunw)
plt.xlabel('Sample')
plt.ylabel('value')
plt.title('Unwarped Filter Coefficients')
plt.show()

#frequency response:
from freqz import freqz
freqz(cunw, 1)

from warpingphase import *
import numpy as np
#warping allpass coefficient:
a = 1.0674 * (2 / np.pi * np.arctan(0.6583 * 32)) ** 0.5 - 0.1916
print 'a = ', a

# ans = 0.85956
# with f_s=32 in kHz. from [1]
# The warped cutoff frequency then is:
fcw = -warpingphase(0.05 * np.pi, 0.85956)
print 'fcw = ', fcw
# fcw = 1.6120; %in radiants
# filter design:
# cutoff frequency normalized to nyquist:
fcny=fcw/np.pi
print 'fcny = ', fcny
# fcny = 0.51312
# python:
c = sp.remez(4, [0, fcny/2.0, fcny/2.0+0.1, 0.5], [1, 0],[1, 100])
#The resulting Impulse Response:
plt.plot(c);
plt.xlabel('Sample')
plt.ylabel('value')
plt.title('Filter Coefficients in Warped Domain')
plt.show()

#The resulting Frequency response:
freqz(c,1)

# Warping Allpass filters:
#Numerrator:
B = [-a.conjugate(), 1]
#Denominator:
A = [1, -a]
# Impulse with 80 zeros:
Imp = np.zeros(80)
Imp[0] = 1
x = Imp

# Y1(z)=A(z), Y2(z)=A^2(z),...
# Warped delays:
y1 = sp.lfilter(B,A,x)
y2 = sp.lfilter(B,A,y1)
y3 = sp.lfilter(B,A,y2)

# Output of warped filter with impulse as input:
yout = c[0]*x+c[1]*y1+c[2]*y2+c[3]*y3
# frequency response:
freqz(yout, 1)

#Impulse response:
plt.plot(yout);
plt.xlabel('Sample')
plt.ylabel('value')
plt.title('Impulse Response of Warped Lowpass Filter')
plt.show()
