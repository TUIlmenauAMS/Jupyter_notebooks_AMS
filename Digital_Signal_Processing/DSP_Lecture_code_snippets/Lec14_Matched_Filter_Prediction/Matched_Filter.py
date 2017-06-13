import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

sig = np.arange(0, 1.1, 0.1)

plt.plot(sig)
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('An Example Signal')
plt.show()

signoise = np.random.rand(20) - 0.5 + np.hstack([np.zeros(4), sig, np.zeros(5)])
plt.plot(signoise)
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('The Example Signal in Noise')
plt.show()

h = sig[::-1] # fliplr
signoisemf = sp.lfilter(h, 1, signoise)
plt.plot(signoisemf)
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('The Example Signal in Noise after Macthed Filtering')
plt.show()
