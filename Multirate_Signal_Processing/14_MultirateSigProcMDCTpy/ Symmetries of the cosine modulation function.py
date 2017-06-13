
# coding: utf-8

# # Python example for the symmetries of the cosine modulation function:

# # Take a modulated analysis filter bank with impulse responses:
# $$\normalsize  {h_k (n)=h(n)⋅cos(\frac{\pi}{4}⋅(k +0.5)⋅(n+0.5))}$$
# with a cosine modulation function like a DCT4. For subband k=0, for N=8 subbands, and for a length of 32, we get:

# In[1]:

get_ipython().magic('matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

c = np.cos(np.pi/8*0.5*(np.arange(32)+0.5))
plt.plot(c)


# ## This image visualizes the following symmetries:

# In[2]:

c[:8]


# ## The second block is identical to flipping and negating the first block:

# In[3]:

c[8:16]


# In[4]:

-np.flipud(c[0:8])


# ## The third block is identical to negating the first block:

# In[5]:

c[16:24]


# ## The last block is identical to flipping the first block:

# In[6]:

c[24:32]


# And so on. We see the following rule: **Every second block is flipped, and after 2 blocks we get a sign change.**
# 
# This is not only true for the first subband, but also for all other subbands k.
# 
