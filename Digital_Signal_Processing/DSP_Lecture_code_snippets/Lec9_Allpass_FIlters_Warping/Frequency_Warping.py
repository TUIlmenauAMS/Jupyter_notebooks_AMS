import numpy as np
import matplotlib.pyplot as plt

#Frequency array between 0 and 20000 Hz in 1000 steps:
f = np.linspace(0,20000,1000)

#Computation of Zwickers Bark approximation formula:
z = 13 * np.arctan(0.00076 * f) + 3.5 * np.arctan((f / 7500.0) ** 2)

#plot Bark over Hertz:
plt.plot(f,z)
plt.xlabel('Frequency in Hertz')
plt.ylabel('Frequency in Bark')
plt.title('Zwicker&Terhard Approximation')
plt.show()