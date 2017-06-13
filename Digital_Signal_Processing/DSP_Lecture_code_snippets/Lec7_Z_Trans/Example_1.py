import matplotlib.pyplot as plt
from freqz import freqz
import numpy as np

A = [1, -0.9]
B = [1]
w = freqz(B,A)
print len(w)

from zplane import zplane 
zplane(B,A)
