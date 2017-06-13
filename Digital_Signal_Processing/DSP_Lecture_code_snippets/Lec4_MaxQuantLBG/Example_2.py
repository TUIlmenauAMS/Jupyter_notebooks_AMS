from scipy.integrate import quad
import numpy as np

Num, Nerr = quad(lambda x:x * np.exp(-0.5 * np.abs(x)), 0, 0.55)
print Num
Den, Derr = quad(lambda x: np.exp(-0.5*np.abs(x)), 0, 0.55)
print Den

print Num/Den
