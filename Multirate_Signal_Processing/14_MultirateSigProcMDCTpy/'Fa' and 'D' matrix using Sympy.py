
# coding: utf-8

# # Sympy  

# In[1]:

from sympy import *


# In[2]:

Fa = Matrix([[0, 1, 4, 0],[2, 0, 0, 3],[3, 0, 0, -2],[0, 4, -1, 0]])
Fa


# In[3]:

z = symbols('z')
D = Matrix([[z**(-1), 0, 0, 0],[0, z**(-1), 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
D


# In[4]:

Fa*D


# * **Here now we have a matrix which only consists of real (or complex) valued elements, which we can now enter into a numerical math package, like MATLAB or Octave or Python. Observe that our time index n for the prototype function runs from the buttom up.**

# ---

# # Example in Python:

# Again assume we have the block length and number of subbands $N=4$, and our baseband prototype impulse response is $h(n)=[1,2,3,4,4,3,2,1]$ . We get the analysis Folding matrix $F_a$ (as above)

# In[5]:

Fa = Matrix([[0, -1, -4, 0],[-2, 0, 0, -3],[-3, 0, 0, 2],[0, -4, 1, 0]])
Fa


# ## and its inverse becomes the Folding matrix for the synthesis, to ensure perfect reconstruction, is $\normalsize F^{(−1)}_a$:

# In[6]:

Fa**(-1)


# ### This is now equal to the synthesis folding matrix $F_s$ , and we can read out the resulting synthesis baseband impulse response as: $$\normalsize g(n) = \big[\frac{1}{17} , \frac{2}{13} , \frac{3}{13} , \frac{4}{17} , \frac{4}{17}, \frac{3}{13}, \frac{2}{13}, \frac{1}{17}\big]$$ 
# 
# ### we can see that its values not quite identical to $h(n)$ . The numerator is the same, but the denominators change.
