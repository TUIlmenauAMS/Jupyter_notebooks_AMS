
# coding: utf-8

# # Python Example
# 
# ## Take the so-called **sine window** or **baseband prototype** for N=4 subbands:

# In[1]:

import numpy as np

h = np.sin(np.pi/8 * (np.arange(8) + 0.5))


# ## Impulse Response

# In[2]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
plt.plot(h)


# ## The corresponding frequency response:

# In[3]:

from freqz import freqz
freqz(h, axisFreqz=[0, np.pi, -50, 20])


# >**We see that this is indeed a low pass filter. It works as both, a window and a low pass prototype filter.**
# 
# ## Now we construct the filter impulse response for subband k=1(second subband):

# In[4]:

h1 = h * np.cos(np.pi/4*(np.arange(8) + 0.5 + 4/2)*(2.5))


# ## And we get the following frequency response:

# In[5]:

freqz(h1, axisFreqz=[0, np.pi, -50, 20])


# **We see that our low pass filter is indeed shifted in frequency to become a bandpass filter.**
