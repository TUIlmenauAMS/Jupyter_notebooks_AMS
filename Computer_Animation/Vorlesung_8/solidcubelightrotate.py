from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#Gerald Schuller, November 2014

def displayFun():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glOrtho(-2.0*64/48.0,2.0*64/48.0,-1.5, 1.5, -0.1, 100)
    gluPerspective(50,64/48.0,0.1, 6)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(2.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #Rotation: glRotate(Angle, rotation axis x, y, z)
    glRotatef(40.0, 0.0,1.0,0.0)
    #glColor3f(0.5,0.5,0.5)
    #glutSolidCube(1.0)
    #glutSolidSphere (1.0, 20, 16);
    glutSolidTeapot(1.0)

    glFlush()

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640,480)
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
    #glEnable(GL_LIGHT1);
    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(displayFun)
    glutMainLoop()
