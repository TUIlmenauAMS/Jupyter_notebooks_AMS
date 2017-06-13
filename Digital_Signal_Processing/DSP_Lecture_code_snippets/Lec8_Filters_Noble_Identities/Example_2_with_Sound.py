import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

N=32
bpass=scipy.signal.remez(N, [0.0, 0.05, 0.1, 0.2, 0.3, 0.5] , [0.0, 1.0, 0.0], weight=[1.0, 1.0, 1.0])

#Plot the magnitude of the frequencyresponse:
fig = plt.figure()
[freq, response] = scipy.signal.freqz(bpass)
plt.plot(freq, np.abs(response))
plt.xlabel('Normalized Frequency (pi is Nyquist Frequency)')
plt.ylabel("Magnitude of Frequency Response")
plt.title("Magnitude of Frequency Response for our Bandbass Filter")
plt.show()

#plotting its impulse response
fig2=plt.figure()
plt.plot(bpass)
plt.title('Impulse Response of our Bandpass Filter')
plt.show()