import numpy as np

x =np.arange(1,10, dtype='float') #lfilter needs float
N = 2

#downsampling
xd = x[::N]
print 'xd', xd

#filtering
import scipy.signal
B = [1,1]
y1 = scipy.signal.lfilter(B, 1, xd)
print 'y1', y1

#upsampling
Bu = np.zeros(3)
Bu[::N] = B
print 'B1', Bu

#filtering the signal before downsamling
yu = scipy.signal.lfilter(Bu, 1, x)
print 'yu', yu

#downsample the filtered signal
y2 = yu[::N]
print 'y2', y2
