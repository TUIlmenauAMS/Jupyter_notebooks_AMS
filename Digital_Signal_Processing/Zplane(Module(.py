
# coding: utf-8

# # This is a module which has a function zplane and can be used for plotting the poles and zeroes of given transfer function (z-plane). It plots the zeros and poles with respect to a given unit circle.

# ### Input: 
# Using this function user provides 2 vectors of values as parameters:
# the variable <i>'nullstellen'(zeros)</i> takes the zeros(roots of the numerator of transfer function) as a vector.
# the variable <i>'pole'</i> takes the poles(roots of the denominator of the transfer function) as a vector.

# ### Output:
# Plot with a unit circle and positions of poles as 'x' and zeros as 'o' on the plot.

# ### Import relevant modules and define the function.

# In[1]:

#Gerald Schuller, June 2016
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def zplane(nullstellen, pole, axis = None):
    """Usage: zplane(zeros, poles)
    plots the location of zeros and poles in the complex z-plane, with a unit circle.
    zeros are circles, poles are crosses.
    zeros, poles: array like, complex."""
    plt.figure()
    #Plotte die Pole in der komplexen Ebene als 'x':
    plt.plot(np.real(pole),np.imag(pole),'x')
    #Plotte die Nullstellen als 'o':
    plt.plot(np.real(nullstellen),np.imag(nullstellen),'o')
    
    
    #passende Axen-Skalierung:
    plt.axis('equal')
    if axis is not None:
        plt.axis(axis)
    
    #Plot unit circle:
    circlere=np.zeros(512)
    circleim=np.zeros(512)
    for k in range(512):
       circlere[k]=np.cos(2*np.pi/512*k)
       circleim[k]=np.sin(2*np.pi/512*k)
    
    plt.plot(circlere,circleim)
    plt.title('Complex z-Plane')
    plt.show()
    return()


# ### Example below:

# In[2]:

#b - list of zeros
#a - list of poles

import numpy as np
# import zplane

b = np.array([.5, -.6, 2.5])
a = np.array([.3, -.3, .1])

zplane(b, a)


# ### Note:
# For using this module file use 'import zplane' and call the function using zplane.zplane(param...). This module is also available in the moodle webpage.
