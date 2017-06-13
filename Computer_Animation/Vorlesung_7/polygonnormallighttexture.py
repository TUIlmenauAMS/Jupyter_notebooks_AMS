from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import cv2

#Gerald Schuller, November 2014
#Skript for demontrating Lights

def displayFun():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glOrtho(-2.0*64/48.0,2.0*64/48.0,-1.5, 1.5, -2, 6)
    gluPerspective(50,64.0/48.0, 1, -10)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(2.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #glColor3f(0.5,0.5,0.5)
    #glutSolidCube(1.0)
    #glutSolidSphere (1.0, 20, 16);

    glColor3f(0.7,0.7,0.7)
   #Polygon und Texturecoordinaten:
    glBegin(GL_POLYGON)
    #glBegin(GL_QUADS)
    #Flaechen-Normale:
    glNormal3f(0.0, 0.0, -1.0);

    glTexCoord2f(0.0, 0.0);
    glVertex3f(-1.0,-1.0, -0.5)
    glTexCoord2f(1.0, 0.0);
    glVertex3f( 1.0,-1.0, -0.5)
    glTexCoord2f(1.0, 1.0);
    glVertex3f( 1.0, 1.0, -0.5)
    glTexCoord2f(0.0, 1.0);
    glVertex3f(-1.0, 1.0, -0.5)

    glEnd();

    glFlush()

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640,480)
    glutCreateWindow("Solid Cube")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.1,0.1,0.1,0.1)

    image=cv2.imread('grass.png')
    #Convert to RGB format:
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #Vertically flip the texture image:
    image=cv2.flip(image,0)
    [ix,iy,c]=image.shape

    glShadeModel (GL_SMOOTH);
    glMaterialfv(GL_FRONT, GL_SPECULAR,GLfloat_4(1.0,1.0,1.0,1.0) )
    glMaterialfv(GL_FRONT, GL_SHININESS, 50.0);
    #color = GLfloat_4(0.8, .8, .8, 1.0);
    #glMaterialfv(GL_FRONT, GL_DIFFUSE, color);
    glLightfv( GL_LIGHT1, GL_AMBIENT, GLfloat_4(0.2, .2, .2, 1.0) );
    glLightfv(GL_LIGHT1, GL_DIFFUSE, GLfloat_3(.8,.8,.8));
    glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(5.0, 5.0, 5.0, 0.0) )
    glLightfv(GL_LIGHT1, GL_POSITION, GLfloat_4(5.0, 5.0, -5.0, 0.0) )

    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT1);
    glEnable(GL_LIGHT0);
    glEnable(GL_DEPTH_TEST)

    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_BGR, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)


    glutDisplayFunc(displayFun)
    glutMainLoop()
