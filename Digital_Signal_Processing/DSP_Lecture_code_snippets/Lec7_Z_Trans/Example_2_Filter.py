import scipy.signal
import matplotlib.pyplot as plt
import numpy as np

#Start with a unit pulse as input x:
x = np.zeros(10)
x[0] = 1

#B and A are given as before:
A = [1, -0.9]
B = [1]

#Now calculate the impulse response:
y = scipy.signal.lfilter(B, A, x)
plt.plot(y, '*')
plt.xlabel('Sample')
plt.ylabel('Value')
plt.show()