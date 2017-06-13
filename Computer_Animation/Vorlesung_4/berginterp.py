from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import random

#script for random interpolation of 2 points in 3D space
#to generate a "mountain" landscape
#Gerald Schuller, Nov. 2014

def randshift(ptleft,ptright):
#plots the two points ptleft and ptright, randomly shifts the middle point, and calls itself on the new point pairs
    smallestdst=0.02;
    roughness=0.7;
    glVertex3fv(ptleft)
    glVertex3fv(ptright)
    #distance:
    distance=np.linalg.norm(ptright-ptleft)
    if (distance>smallestdst):
       midpoint=0.5*(ptleft+ptright)
       midpoint[1]=midpoint[1]+distance*roughness*(random.random()-0.5)
       randshift(ptleft,midpoint)
       randshift(midpoint,ptright)


def displayFun():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
#Orthogonale Projektionsmatrix,
#glOrtho(left, right, bottom, top, znear, zfar);
    glOrtho(-3.0,3.0,-1.5, 1.5, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

#Position der virtuellen Kamera:
#gluLookAt( eyeX , eyeY , eyeZ , centerX , centerY , centerZ , upX , upY , upZ )
    gluLookAt(0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0,0.0,0.0)
 #Kreis aus Punkten, Vertices berechnet innerhalb von glBegin und glEnd:
    glPointSize(2)
    glBegin(GL_POINTS)

    #2 Punkte die eine Line aufspannen:
    P0=np.array([-2.0,0.0,0.0])
    #glVertex3fv takes an Array or Matrix as input!:
    #glVertex3fv(P0)
    P1=np.array([2.0,0.0,0.0])
    #glVertex3fv(P1)


    glColor3f(0.0,0.0,0.0)
    randshift(P0,P1)

    glEnd();

    glFlush()

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640,480)
    glutCreateWindow("3D")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glClearColor(1.0,1.0,1.0,0.0)
    glutDisplayFunc(displayFun)
    glutMainLoop()
