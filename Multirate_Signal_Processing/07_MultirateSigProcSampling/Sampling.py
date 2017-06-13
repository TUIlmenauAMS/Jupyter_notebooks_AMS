
# coding: utf-8

# # Python Example: Sampling
# Make a sine wave which at 44100 Hz sampling rate has a frequency of 400 Hz at 1 second duration. Hence we need 44100 samples, and 400 periods of our sinusoid in this second.
# 
# `- Gerard Schuler`

# ## Import the relevant modules:

# In[1]:

import numpy as np

s = np.sin(2*np.pi*400*np.arange(0,1,1./44100))

import sound
sound.sound(s*2**15, 44100)


# ## Plot the first 1000 samples:

# In[2]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt

plt.plot(s[:1000])


# ## Plot the first 100 samples:

# In[3]:

plt.plot(s[:100])


# * **Now we can multiply this sine tone signal with a unit pulse train, with N=8.**
# 
# ## We generate the unit impulse train:

# In[4]:

delta = np.zeros(44100)
delta[0::8] = 1
plt.plot(delta[:100])
plt.xlabel('n')
plt.ylabel('delta(n)')


# ## Listen to delta signal:

# In[5]:

sound.sound(delta*2**15, 44100)


# ## See the resulting dirac train in the frequency domain:

# In[6]:

from freqz import freqz

freqz(delta)


# ## The multiplication with the unit impulse train:

# In[7]:

sdu = s * delta


# * **(This multiplication is also called „frequency mixing“). Now plot the result, the first 100 samples:**

# In[8]:

plt.plot(sdu[0:100])


# * **This is our signal still with the zeros in it.**
# 
# ## Now take a look and compare the spectra, first the original signal s:

# In[9]:

freqz(s)


# **The upper two plots show the magnitude of the frequency spectrum of our signal, the lowest plot is its phase. Observe that the frequency axis (horizontal) is a normalized frequency, normalized to the Nyquist frequency, in our case 22050 Hz. Hence our sinusoid should appear as a peak at normalized frequency 400/22050=0.018141, which we indeed see.**

# ## Now we can compare this to our signal with the zeros, sdu:

# In[10]:

freqz(sdu)


# **Here we can see the original line of our 400 Hz tone, and now also the 7 new aliasing components. Observe that always 2 aliasing components are close together. This is because the original 400 Hz tone also has a spectral peak at the negative frequencies, at -400 Hz, or at normalized frequency -0.018 (which is 400/22050).**
# 
# **Observe the artifacts at levels of about 20 dB and below: those are measurement artifacts that result from the limited attenuation in the stop bands of the filter bank used inside the freqz function, because it uses a finite (rectangular) window, usually of size 1024 samples, hence *Gibbs Phenomenon* applies.**

# ## Now also listen to the signal with the zeros:

# In[11]:

sound.sound(sdu*2**15,44100)


# **Here you can hear that it sounds quite different from the original, because of the strong aliasing components!**
