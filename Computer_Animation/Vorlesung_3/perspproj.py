#from sympy import * 
from numpy import *

#Script for perspective projection matrix
#Gerald Schuller, Nov. 2014

#r=symbols('r')
#l=symbols('l')
#t=symbols('t')
#b=symbols('b')
#n=symbols('n')
#f=symbols('f')

f=1.0
aspect=2.0
znear=5.0
zfar=15.0

#Perspektivische Projektions-Matrix:
P=matrix([[f/aspect,0,0,0],
[0,f,0,0],
[0,0,(zfar+znear)/(znear-zfar), (2*zfar*znear)/(znear-zfar)],
[0,0,-1.0,0]])
#Vertex in der rechten oberen nahen Ecke:
V=matrix([[aspect/f*znear],[1/f*znear],[-znear],[1.0]])
print(P)
print(V)
#Projektion:
Pr=P*V
#Normierung auf homogene Koordinate w=Pr[3]=1:
print(Pr/Pr[3])
