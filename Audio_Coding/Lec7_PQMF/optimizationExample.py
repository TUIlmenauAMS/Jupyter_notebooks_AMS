#Optimization example, see also:
#https://docs.scipy.org/doc/scipy-0.18.1/reference/optimize.html
#Gerald Schuller, Nov. 2016
#run it with "python optimizationExample.py" in a termina shell
#or type "ipython" in a termina shell and copy lines below:

import numpy as np
import scipy.optimize as optimize
from functionexamp import functionexamp

#Example for 2 unknowns, args: function-name, starting point, method:
from functionexamp import *
xmin = optimize.minimize(functionexamp, [-1.0, -3.0], method='CG')
print xmin