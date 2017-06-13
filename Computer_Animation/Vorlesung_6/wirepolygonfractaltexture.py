from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import cv2
import numpy as np

#Gerald Schuller, November 2014
#Skript for demonstrating procedural texture, the Mandelbrot Set

def displayFun():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0*64/48.0,2.0*64/48.0,-1.5, 1.5, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(2.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glColor3f(0.7,0.7,0.7)
#Polygon und Texturecoordinaten:
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0);
    glVertex3f(-1.0,-1.0, 0.0)
    glTexCoord2f(1.0, 0.0);
    glVertex3f( 1.0,-1.0, 0.0)
    glTexCoord2f(1.0, 1.0);
    glVertex3f( 1.0, 1.0, 0.0)
    glTexCoord2f(0.0, 1.0);
    glVertex3f(-1.0, 1.0, 0.0)

    glEnd();
    glFlush()

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640,480)
    glutCreateWindow("Textured Polygon")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glEnable(GL_TEXTURE_2D)
    #glEnable(GL_CULL_FACE)
    glClearColor(1.0,1.0,1.0,0.0)

   # image=cv2.imread('TUI.png')
    #Convert to RGB format:
   # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #Vertically flip the texture image:
   # image=cv2.flip(image,0)
   # [ix,iy,c]=image.shape
   # print(image[0][0][0])

#Apfelmaennchen als Textur:
    image=np.ones((512,512,3))*0
    [ix,iy,c]=image.shape
    print(c)
    for x in range(ix):
       for y in range(iy):
          #set starting point in complex domain between -2 and 2:
          c=(float(x)/ix-0.5)*4 + 1j*(float(y)/iy-0.5)*4

          #start iteration:
          z=0;
          for it in range(10):
             z=z*z+c

          ma=np.minimum(np.abs(z),200.0)/200.0*255;
          #print(ma)
          image[y,x,0]=ma;
          #image[x,y,1]=np.abs(255-2*ma)
          #image[x,y,2]=np.abs(255-ma)


    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    glutDisplayFunc(displayFun)
    glutMainLoop()
