#Program to display the variable mix of the 3 primary colors
#Gerald Schuller, May 2015

import numpy as np
import scipy.signal
import cv2


#Rows and columns of image:
rows=200
cols=250
print(rows,cols)
image=np.zeros((rows,cols,3));

#Default color factors:
b=0.5
g=0.5
r=0.5

bim=np.zeros((rows,cols,3))
#print(bim.shape)
bim[50:150,30:130,0]=np.ones((100,100))
gim=np.zeros((rows,cols,3))
gim[50:150,100:200,1]=np.ones((100,100))
rim=np.zeros((rows,cols,3))
rim[100:200,60:160,2]=np.ones((100,100))

while(True):
    #print(r,g,b)
    image=b*bim+g*gim+r*rim;
    cv2.putText(image,"Red +-: a/y, Green: s/x, Blue: d,c", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,128,128))
    v2.putText(image,"Red:"+str(r)+" Green:"+str(g)+" Blue:"+str(b)+", quit:q", (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,128,128))
    
    cv2.imshow('Color Mixture',image)

    
    
    
    key=cv2.waitKey(1) & 0xFF;
    if key == ord('a'):
       r= r+0.1;
       r=np.clip(r,0,1)
    if key == ord('y'):
       r= r-0.1;
       r=np.clip(r,0,1)
    if key == ord('s'):
       g= g+0.1;
       g=np.clip(g,0,1)
    if key == ord('x'):
       g= g-0.1;
       g=np.clip(g,0,1)
    if key == ord('d'):
       b= b+0.1;
       b=np.clip(b,0,1)
    if key == ord('c'):
       b= b-0.1;
       b=np.clip(b,0,1)
    if key == ord('q'):
        break

# When everything done, release the capture

cv2.destroyAllWindows()
