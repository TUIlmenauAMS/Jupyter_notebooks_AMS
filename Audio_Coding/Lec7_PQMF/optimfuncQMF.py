import numpy as np
import scipy as sp
import scipy.signal as sig

def optimfuncQMF(x):
    """Optimization function for a PQMF Filterbank
    x: coefficients to optimize (first half of prototype h because of symmetry)
    err: resulting total error
    """
    N = 4 #4 subbands
    h = np.append(x, np.flipud(x))
    f, H_im = sig.freqz(h)
    H = np.abs(H_im) #only keeping the real part
    
    posfreq = np.square(H[0:512/N])
    
    #Negative frequencies are symmetric around 0:
    negfreq = np.flipud(np.square(H[0:512/N]))
    
    #Sum of magnitude squared frequency responses should be closed to unity (or N)
    unitycond = np.sum(np.abs(posfreq + negfreq - 2*(N*N)*np.ones(512/N)))/512
    
    #plt.plot(posfreq+negfreq)
    
    #High attenuation after the next subband:
    att = np.sum(np.abs(H[1.5*512/N:]))/512
    
    #Total (weighted) error:
    err = unitycond + 100*att
    return err