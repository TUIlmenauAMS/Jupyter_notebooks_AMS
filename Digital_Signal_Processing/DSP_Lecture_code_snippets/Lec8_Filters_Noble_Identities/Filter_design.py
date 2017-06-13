import scipy.signal as sp
import matplotlib.pyplot as plt

N=8 #number of taps
F = [0.0, 0.5/2 - 0.05, 0.5/2, 0.5] #Frequencyt bands for pass band, trnasition band and stop band
A = [1.0, 0.0]#Desired response in passband and stopband
W = [1, 100]

hmin = sp.remez(N, F, A, weight=W)

#plot impulse response
plt.plot(hmin)
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('Impulase Response')
plt.show()

#plot freqeuncy response
from freqz import freqz
freqz(hmin)