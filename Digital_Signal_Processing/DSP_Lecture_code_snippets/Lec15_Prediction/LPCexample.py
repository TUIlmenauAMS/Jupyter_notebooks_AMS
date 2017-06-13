import numpy as np
from sound import *
import matplotlib.pyplot as plt
import scipy.signal as sp

x, fs = wavread('speech8kHz.wav')

x = np.array(x,dtype=float)/2**15
print np.size(x)

sound(2**15*x,fs)

len0 = np.max(np.size(x))

e = np.zeros(np.size(x)) 

blocks = np.int(np.floor(len0/640)) 

state = np.zeros(10)

for m in range(0,blocks):
	A = np.zeros((630,10)) #trick: up to 630 to avoid zeros in the matrix
	for n in range(0,630):
		A[n,:] = x[m*640+n+np.arange(10)]
     
	#Construct our desired target signal d, one sample into thefuture:
	d=x[m*640+np.arange(10,640)];
	
	#Compute the prediction filter:
	h = np.dot(np.dot(np.linalg.inv(np.dot(A.transpose(), A)), A.transpose()), d)
	hperr = np.hstack([1, -np.flipud(h)])
	e[m*640+np.arange(0,640)], state = sp.lfilter(hperr,1,x[m*640+np.arange(0,640)], zi=state)
	 
print "The average squared error is:", np.dot(e.transpose(),e)/np.max(np.size(e))

print "Compare that with the mean squared signal power:", np.dot(x.transpose(),x)/np.max(np.size(x))

print "The Signal to Error ratio is:", np.dot(x.transpose(),x)/np.dot(e.transpose(),e)

sound(2 ** 15 * e, fs)

plt.plot(np.divide(x, float(np.max(x))))#np.abs(x)))))
plt.plot(e,'r')
plt.xlabel('Sample')
plt.ylabel('Normalized Value')
plt.legend(('Original','Prediction Error'))
plt.show()

