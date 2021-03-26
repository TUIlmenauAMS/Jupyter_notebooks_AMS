#Gerald Schuller, March 2021
#With translation and rotation animation
#Stores the animation in a video

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import numpy as np
import cv2

from PIL import Image


rotationAngle=0.0

def displayFun():
    global rotationAngle
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glOrtho(-2.0*64/48.0,2.0*64/48.0,-1.5, 1.5, -0.1, 100)
    gluPerspective(25.0,640/480.0,0.1, 6)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #gluLookAt( eyeX , eyeY , eyeZ , centerX , centerY , centerZ , upX , upY , upZ )
    gluLookAt(2.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    #camera at coordinate origin, shifted in z-axis away from object:
    #gluLookAt(0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   
    
    #virtual world coordinates of object (from face detector):
    #glTranslate(  0.0084955752212389386, -0.083539823008849559, -1.3274336283185841)
    #glTranslate(0.089523809523809533, 0.081904761904761911, -1.7857142857142858)
    #glTranslate(-0.11692307692307692, -0.047179487179487181, -1.9230769230769231)
    #glTranslate(0.01971014492753623, -0.01816425120772947, -0.7246376811594203)
    glRotate(rotationAngle,0,1,0)
    glTranslate(0.0, 0.0, -0.5)

    #glPushMatrix()
    
    #Breite des Kopfes/Objektes: 0.16
    #glColor3f(0.5,0.5,0.5)
    #glutSolidCube(0.16)
    #glutSolidSphere (0.16, 20, 16);
    glutSolidTeapot(0.16)
    #Increase rotation angle:
    rotationAngle+=1.0

    glFlush()
    #Read frame:
    screenshot = glReadPixels(0,0,width,height,GL_RGB,GL_UNSIGNED_BYTE)
    #Convert from binary to cv2 numpy array:
    snapshot = Image.frombuffer("RGB",(width,height),screenshot,"raw","RGB",0,0)
    snapshot= np.array(snapshot)
    snapshot=cv2.flip(snapshot,0)
    #write frame to video file:
    out.write(snapshot)
    if rotationAngle>90:  #End movie
       glutLeaveMainLoop()
       out.release()
       print("Exit")

    
def idleFun():
        time.sleep(0.05) #wait time in seconds, 0.05 is ca. 20 frames per second
        glutPostRedisplay()
        
def closevideo():
        out.release()
        print("Exit")

if __name__ == '__main__':

    #Set up video:
    width=640
    height=480
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    #Open video output file:
    out = cv2.VideoWriter('videoout.mp4',fourcc, 20.0, (width,height))
    
    glutInit()
    glutInitWindowSize(width,height)
    glutCreateWindow("Solid Cube")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glClearColor(0.1,0.1,0.1,0.1)
    #Hier wird der Shader definiert, entweder GL_FLAT (stueckweise konstant) oder GL_SMOOTH (ueberblenden):
    glShadeModel (GL_SMOOTH);
    #Die Farbe des spiegelnd reflektieren Lichts:
    glMaterialfv(GL_FRONT, GL_SPECULAR,GLfloat_4(1.0,1.0,1.0,1.0))
    #Wie stark spiegelnd die Oberflaeche ist:
    glMaterialfv(GL_FRONT, GL_SHININESS, 50.0);
    #http://glprogramming.com/red/chapter05.html
    #http://pydoc.net/Python/PyOpenGL-Demo/3.0.1b1/PyOpenGL-Demo.GLE.maintest/:
    #glLightfv (GL_LIGHT0, GL_POSITION, lightOnePosition)
    #glLightfv (GL_LIGHT0, GL_DIFFUSE, lightOneColor)
    #Licht Nr.0:
    glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(-0.0, 5.0, -5.0, 1.0))
    #Diffuse: Licht von einem Punkt (GL_POSITION) in alle Richtungen, mit Intensitaet und 
    #Farbe als RGB im Argument:
    glLightfv (GL_LIGHT0, GL_DIFFUSE, GLfloat_3(.8,.1,.1))
    #Umgebungslicht-Anteil der Quelle, mit Umgebungslicht-Intensitaet und Farbe als RGB:
    glLightfv( GL_LIGHT0, GL_AMBIENT, GLfloat_4(0.5,0.2,0.2, 1.0) );
    #Licht Nr. 1:
    glLightfv(GL_LIGHT1, GL_POSITION, GLfloat_4(5.0, 5.0, 5.0, 1.0) )
    #glLightfv(GL_LIGHT1, GL_POSITION, GLfloat_4(-0.0, 5.0, -5.0, 1.0))
    glLightfv(GL_LIGHT1, GL_DIFFUSE, GLfloat_3(.8,.99,.8));
    #Umgebungslicht-Anteil der Quelle:
    glLightfv( GL_LIGHT1, GL_AMBIENT, GLfloat_4(0.5, .7, .5, 1.0) );

    #Lichter Einschalten:
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_LIGHT1);
    glEnable(GL_DEPTH_TEST)
    #import atexit
    #atexit(closevideo);
    glutDisplayFunc(displayFun)
    glutIdleFunc(idleFun)
    glutMainLoop()
    
    """
    for i in range(250):
       glutMainLoopEvent()
    """
    
    
