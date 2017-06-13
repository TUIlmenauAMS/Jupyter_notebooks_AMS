
# coding: utf-8

# # Example for the extraction of the Fa Matrix from the MDCT polyphase matrix.

# ## Import Scipy and Sympy:

# In[1]:

from sympy import *
from scipy import *


# In[2]:

z=symbols('z') 
N=4 


# ## Baseband prototype filter h(n):

# In[3]:

h = symbols('h:8')
print( 'h:', h) 


# > **MDCT Polyphase matrix H. Since each column contains the time-reversed impulse response, we need the "N-1-n" instead of the "n":  **
# 
# ## Start with a NxN matrix of zeros: 

# In[4]:

H = Matrix(zeros((N,N)))


# > **range(0,N) produces indices from 0 to N-1. **
# 
# ## We compute H using eq. (1) and (2):

# In[5]:

for n in range(0,N): 
    for k in range(0,N): 
        H[n,k] = h[N-1-n]*cos(pi/N*(N-1-n + N/2 + 0.5)*(k+0.5)) + z**(-1)*h[2*N-1-n]*cos(pi/N*(2*N-1-n+N/2+0.5)*(k+0.5)) 


# ## Transform matrix T for the DCT4: 

# In[6]:

T=Matrix(zeros((N,N)))
for n in range(0,N): 
    for k in range(0,N): 
        T[n,k]=cos(pi/N*(n+0.5)*(k+0.5))


# ## Compute the sparse Fa matrix: 

# In[7]:

Fa = H * (T ** (-1)) 


# ## Print the H matrix with 1 digit after the decimal point and replacement of very small number by 0: 

# In[8]:

print( "H=") 
print( H.evalf(1,chop=True))


# ## Print the Fa matrix with 1 digit after the decimal point and replacement of very small number by 0: 

# In[9]:

print( "Fa=") 
print( Fa.evalf(1,chop=True))

