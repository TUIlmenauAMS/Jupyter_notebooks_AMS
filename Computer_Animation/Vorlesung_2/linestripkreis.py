from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

#Script for parametric function description of a circle
#Gerald Schuller, Oct. 2014

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
    gluLookAt(2.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0,0.0,0.0)
    #Kreis aus Liniensteucken, Vertices berechnet innerhalb von glBegin und glEnd:
    glBegin(GL_LINE_STRIP)
    #Alternativ: Kreis aus Punkten:

    #glPointSize(5)
    #glBegin(GL_POINTS)

    for f in np.linspace(0,2*np.pi,40):
      glVertex3f(np.cos(f),np.sin(f),0);
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
