#from sympy import *
from numpy import *

#Script for orthogonal projection matrix
#Gerald Schuller, Nov. 2014

#r=symbols('r')
#l=symbols('l')
#t=symbols('t')
#b=symbols('b')
#n=symbols('n')
#f=symbols('f')

r=10.0
l=-10.0
t=5.0
b=-5.0
n=5.0
f=15.0

P=matrix([[2.0/(r-l),0,0,-(r+l)/(r-l)],
[0,2.0/(t-b),0,-(t+b)/(t-b)],
[0,0,(-2.0)/(f-n), -(f+n)/(f-n)],
[0,0,0,1.0]])

V=matrix([[l],[b],[-n],[1.0]])
print(P)
print(V)

print(P*V)
