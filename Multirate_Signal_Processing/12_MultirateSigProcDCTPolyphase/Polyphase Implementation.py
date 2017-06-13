
# coding: utf-8

# # Python Example
# We would like to **low pass filter** a signal, with a subsequent **downsampling** by a factor of $N=2$.
# 
# First the **direct implementation**, which is computationally more expensive, because we also compute the values which are discarded by the down sampler,

# ## Simple signal:

# In[1]:

import numpy as np

x = np.arange(1, 21)
x


# ## Simple low pass filter impulse response:

# In[2]:

h = np.arange(1,5)
h


# ## Low-pass filtered signal:

# In[3]:

xlp = np.convolve(x,h)
xlp


# ## Downsampled signal:

# In[4]:

xlpds = xlp[1::2]
xlpds


# **Now using the polyphase implementation, dividing our signal and impulse response in blocks. We implement ${\normalsize{y(m)= \sum\limits_{n=0}^{2-1}x_n(m)∗h_n(m)}}$. First the polyphase representation of our input signal, xn, as a sequence of blocks,**

# In[5]:

xn = np.reshape(x, (len(x)/2, 2))
xn


# **Next we create the polyphase representation of our low pass filter, hn, again as a sequence of its blocks, including the flipping for the analysis side,**

# In[6]:

hn = np.fliplr(np.reshape(h, (len(h)/2, 2)))
hn


# * **low pass filtered and down sampled result,**

# In[7]:

xlpds = (np.convolve(xn[:,0], hn[:,0]) + np.convolve(xn[:,1],hn[:,1]))
xlpds


# **Observe:** This is the same result as the direct implementation, but without computing the samples which are not passed by the down sampler!
# 
# We have phase $n_0 =N −1=1$ in our example for the downsampled signal, but we could equally obtain phase 0, if we construct our polyphase vector xp accordingly (with a leading zero).
