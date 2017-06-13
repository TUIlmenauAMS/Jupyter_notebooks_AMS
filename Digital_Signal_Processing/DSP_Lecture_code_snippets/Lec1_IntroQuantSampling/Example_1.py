import numpy as np
q = 0.1 #stepsize
x = np.array([0.012, 1.234, 2.456, 3.789])
print x
index = np.round(x/q)
print index
reconstr = index * q
print reconstr