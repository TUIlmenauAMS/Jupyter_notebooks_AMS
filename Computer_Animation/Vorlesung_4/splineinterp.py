from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import scipy.interpolate as interp

#script for Spline interpolation of a few points in 3D space
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
    
    #5 Punkte die ein Polygon aufspannen:
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
    
#Spline interpolation: 
    u=np.arange(0,5)
    x=np.array([P0[0],P1[0],P2[0],P3[0],P4[0]])
    y=np.array([P0[1],P1[1],P2[1],P3[1],P4[1]])
    #Cubic Spline:
    fx = interp.interp1d(u, x,kind='cubic')
    fy = interp.interp1d(u, y,kind='cubic')
    #fx = interp.interp1d(u, x,kind='quadratic')
    #fy = interp.interp1d(u, y,kind='quadratic')
    #fx = interp.interp1d(u, x,kind='linear')
    #fy = interp.interp1d(u, y,kind='linear')
    #B-Spline:
    #tckx = interp.splrep(u, x, k=3)
    #tcky = interp.splrep(u, y, k=3)
    for u in np.linspace(0.1,3.9,30): 
      #spline interpolation of the 5 points, not inside the convex hull:
      glVertex3f(fx(u),fy(u),0.0);
      #B-spline interpolation of the 3 points, inside the convex hull:
      #glVertex3f(interp.splev(u,tckx),interp.splev(u,tcky),0.0);
      
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
