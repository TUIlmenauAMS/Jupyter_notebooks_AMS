import numpy as np
from sound import *
import matplotlib.pyplot as plt

x, fs = wavread('speech8kHz.wav')

x = np.array(x,dtype=float)/2**15
print np.size(x)
e = np.zeros(np.size(x))
h = np.zeros(10)

for n in range(10, len(x)):
    
    #prediction error and filter, using the vector of the time reversed IR:
    e[n] = x[n] - np.dot(x[n-10+np.arange(0,10)], np.flipud(h))
    
    #LMS update rule, according to the definition above:
    h = h + 1.0* e[n]*np.flipud(x[n-10+np.arange(0,10)]

print "Mean squared prediction error:", np.dot(e, e) /np.max(np.size(e))
	
sound(2**15*e, fs)

plt.figure()
plt.plot(x)
plt.plot(e,'r')
plt.xlabel('Sample')
plt.ylabel('Normalized Sample')
plt.title('Least Mean Squares (LMS) Online Adaptation')
plt.legend(('Original','Prediction Error'))
plt.show()


#decoder

h = np.zeros(10);
xrek = np.zeros(np.size(x));
for n in range(10, len(x)):
    if n> 4000 and n< 4010:
       print "decoder h: ", h
    P=np.dot(xrek[n-10+np.arange(10)], np.flipud(h))
    xrek[n] = e[n] + P 
    #LMS update:
    h = h + 1.0 * e[n]*np.flipud(xrek[n-10+np.arange(10)]);
plt.plot(xrek)
plt.show()
#Listen to the reconstructed signal:
sound(2**15*xrek,fs)

#Listen to the reconstructed signal:
sound(2**15*xrek, fs)