import numpy as np
import matplotlib.pyplot as plt

r = 480
c = 640

# For rows

Mr = np.ones((r,1))
Mr[(r/4.0):r,0] = np.zeros((3.0/4.0*r))
#For columns
Mc = np.ones((1,c))
Mc[0, (c/4.0):c] = np.zeros((3.0/4.0*c))
#Together
M = np.dot(Mr, Mc)

plt.imshow(M)
plt.title("Tiefpass Masske fuer die 2D-DCT")
plt.show()
