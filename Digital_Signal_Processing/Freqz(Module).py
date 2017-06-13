
# coding: utf-8

# # This is a module which has a function freqz which can be used to plot the frequency response of a filter or a digital signal and outputs the plot for frequency response and phase response for the given filter or signal.

# ### Input:
# Inputs for the function freqz are as follows:
# ##### 'b' - vector of Filter coefficients in the numerator of its transfer function
# ##### 'a' - vector of Filter coefficients in the denominator of its transfer function(default value is 1 for FIR filter)
# ##### 'whole' - boolean parameter for plotting the frequency/phase for the complete timeperiod(cycle/2pi)
# ##### axisFreqz - vector of values for scaling axes of Frequency response. Vector structure: [xmin, xmax, ymin, ymax].
# ##### axisPhase - vector of values for scaling axes of Phase response. Vector structure: [xmin, xmax, ymin, ymax].

# ### Output:
# Shows a plot with twos subplots of frequency response on top and phase response at the bottom for the given signal of for filter coefficients provided.

# ### Import the relevant modules and define the function.

# In[1]:

# Module for show impulse rsponse answer
# Julia Peter, Mathias Kuntze
#Modified, Gerald Schuller, Nov. 2016

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sp

def freqz(b, a=1, whole = False, axisFreqz = None, axisPhase = None):
    
    w, h = sp.freqz(b, a, worN=512, whole=whole)
    #w = w/np.pi
    fig = plt.figure()
    plt.title('Digital filter frequency response')
    plt.subplot(2,1,1)
    
    plt.plot(w, 20 * np.log10(abs(h)), 'b')
    plt.ylabel('Amplitude (dB)')
    plt.xlabel('Normalized Frequency')
    plt.grid()
    if axisFreqz is not None:
        plt.axis(axisFreqz)
    
    plt.subplot(2,1,2)
    #angles = np.unwrap(np.angle(h))
    angles = np.angle(h)
    plt.plot(w, angles, 'g')
    plt.ylabel('Angle (radians)')
    plt.xlabel('Normalized Frequency')
    plt.grid()

    if axisPhase is not None:
        plt.axis(axisPhase)
    
    plt.show()
    return h

