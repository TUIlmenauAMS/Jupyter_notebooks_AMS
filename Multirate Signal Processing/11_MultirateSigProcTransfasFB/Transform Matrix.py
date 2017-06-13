
# coding: utf-8

# # Python example for Transform matrix:
# ## Take a DFT of size N =4 . Its transform matrix T can be obtained with

# In[1]:

import numpy as np
import warnings
warnings.filterwarnings('ignore')

T = np.fft.fft(np.eye(4))
T


# **Observe that we have complex values in the transform, and hence obtain complex valued filters. To evaluate complex valued filters, we need the full circle in the frequency domain, from 0 to 2pi.**
# 
# **If we want to obtain the frequency response of subband k=1 of this DFT filter bank, we take the second column, time-reverse it, and plot the frequency response with freqz. Because Python starts indexing at 1, we need the index 2 for the subband k. In Python, we use "fft", which stands for Fast Fourier Transform, the fast implementation of the DFT, and command "freqz" uses the fft function internally,**

# In[2]:

from freqz import freqz
freqz(np.flipud(T[:,1]), whole=True)


# Observe: We have a bad stopband attenuation (less than 20dB).
# 
# Also observe: The frequency axis is going from 0 to 2 (instead of just 1). This is because we have a complex impulse response. The normalized frequency 2 is the sampling frequency 2 π . Since we have a 2 π periodic frequency, this is identical to frequency 0, and the frequencies from 1 to 2 can also be seen as the negative frequencies from -1 to 0. This shows that this filter has a pass band at the positive frequencies, but not at the negative frequencies. 
# The equivalent passband at the negative frequencies is obtained from subband k=3,

# In[3]:

freqz(np.flipud(T[:,3]), whole=True)


# Observe: This looks like the frequency mirrored version of the filter for k=1. This also shows how to separate positive and negative frequencies.

# ---

# # Example Transform as Filter Bank:
# Now we show in an example that the **transform** is indeed a special case of **a critically sampled filter bank** with the above computed filters.

# ## Take the example signal of length 8:

# In[4]:

x = np.sin(2 * np.pi/8 * np.arange(8)) 


# ## and its decomposition into blocks of length 4:

# In[5]:

xm = np.zeros((2,4))
xm[0,:] = x[0:4]
xm[1,:] = x[4:8]
xm


# In[6]:

T = np.fft.fft(np.eye(4))
T


# ## We obtain the transformed blocks with:

# In[7]:

yt = np.dot(xm, T)
np.around(yt, decimals=4)


# Here, each row contains the spectrum of each corresponding block.
# 
# Now we process the input signal **`x`** through a critically sampled filter bank with the equivalent filter impulse responses, the transform matrix columns, flipped up-down, and down-sampled with the last phase of the blocks, $n_0 =N −1=3$ (as it appeared in our derivation of the equivalent impulse responses),

# In[8]:

import scipy.signal as sp
y = np.zeros((2,4), dtype=complex)
for k in range(4):
    # in Octave: downsample(filter( flipud(T(:,k)),1,x).T,4,3)
    # Downsampling by 4 with an offset of 3 samples(indexed by 0, 1, & 2)
    y[:,k] = (sp.lfilter(np.flipud(T[:,k]).T, 1, x))[3::4]
    
# Set the complex terms(real or imaginary) less than 10^(-4) as zero
np.imag(y)[np.abs(np.imag(y))<= 1e-4], np.real(y)[np.abs(np.real(y))<= 1e-4] = 0, 0
#Display the result in y
np.around(y, decimals=4)


# We can see that **`yt`** from the **transform** and **`y`** from the critically sampled **filter bank** are indeed the **same**!
# 
# **In conclusion**: We see that a **transform** is a special case of a filter bank. The tool of reading out the impulse responses from a transform matrix allows us to **analyze the resulting filters**, and to judge if they fulfill our requirements.
