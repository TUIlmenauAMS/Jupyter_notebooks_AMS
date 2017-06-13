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