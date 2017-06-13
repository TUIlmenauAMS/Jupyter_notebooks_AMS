#function example with several unknowns (variables) for optimization
#Gerald Schuller, Nov. 2017

import numpy as np
def functionexamp(x):
	#x: array with 2 variables
	
	y = np.sin(x[0] + x[1])
	return y