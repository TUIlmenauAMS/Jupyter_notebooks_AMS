import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 6.28, 100) #100 points in 0 to 6.28
s = np.sin(t)
plt.plot(t, s)
plt.show()
