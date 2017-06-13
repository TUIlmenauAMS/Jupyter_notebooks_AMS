
# coding: utf-8

# ## This is a python module which generates warping phase of an allpass filter.

# * Input - namely two parameters as follows:
#   * w - vector of normalized frequencies i.e., from 0 to $\pi$
#   * a - allpass coefficient
# * Output
#   * wy - warped frequencies vector

# In[1]:

import numpy as np
# import matplotlib.pyplot as plt
def warpingphase(w, a):
    #produces (outputs) phase wy for an allpass filter
    #w: input vector of normlized frequencies (0..pi)
    #a: allpass coefficient
    #phase of allpass zero/pole :
    theta = np.angle(a);
    #magnitude of allpass zero/pole :
    r = np.abs(a);
    wy = - w - 2 * np.arctan((r*np.sin(w - theta))/(1 - r*np.cos(w - theta)))
    return wy

