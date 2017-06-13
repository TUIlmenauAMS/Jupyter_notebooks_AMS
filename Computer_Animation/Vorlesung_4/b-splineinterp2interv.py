from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

#script for B-Spline interpolation of a few points in 3D space, for 2 intervals
#Gerald Schuller, Nov. 2014

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
    glPointSize(5)
    glBegin(GL_POINTS)

    #5 Punkte die ein Polygon aufspannen, und 2 B-Spline Intervalle umfassen:
    P0=np.array([-1.0,-1.0,0.0])
    #glVertex3fv takes an Array or Matrix as input!:
    glVertex3fv(P0)
    P1=np.array([1.0,-1.0,0.0])
    glVertex3fv(P1)
    P2=np.array([0.0,0.5,0.0])
    glVertex3fv(P2)
    P3=np.array([-1.0,0.5,0.0])
    glVertex3fv(P3)
    P4=np.array([-1.5,0.35,0.0])
    glVertex3fv(P4)

    glColor3f(0.0,0.0,0.0)
    f = 0.0;
    for u in np.linspace(0.1,0.9,10):
      b0=1.0/6*u**3
      b1=1.0/6*(-3*u**3 + 3*u**2 + 3*u + 1)
      b2=1.0/6*(3*u**3 - 6*u**2 + 4)
      b3=1.0/6*(-u**3 + 3*u**2 - 3*u + 1)
      print(b0,b1,b2,b3)
      print(b0+b1+b2+b3)
      #linear interpolation of the 4 points inside the convex hull:
      #first interval:
      glVertex3fv(b0*P0+b1*P1+b2*P2+b3*P3);
      #second interval:
      glVertex3fv(b0*P1+b1*P2+b2*P3+b3*P4);

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
