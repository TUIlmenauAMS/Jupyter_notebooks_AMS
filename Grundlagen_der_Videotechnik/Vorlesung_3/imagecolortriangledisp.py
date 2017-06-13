import numpy as np
import cv2
import matplotlib.pyplot as plt

#Program to display all possible display colors on the screen in a color triangle

#make frames of 300x300 pixels with 3 equal color components:
frame=np.zeros((300,300,3))
#300 values between 0 and 1 for the entire intensity range on a diagonal matrix:
d=np.diag(np.linspace(1,0,300))
#Matrix with  values from 0 to 1 from bottom to top:
A=np.dot(d,np.ones((300,300)))
#Red component: Transposed, increasing values from 0 to 1 from left to right:
frame[:,:,2]=np.fliplr(A.T)
#Green component: increasing values from 0 to 1 from bottom to top:
frame[:,:,1]=A
#Blue component: 1-R-G: 
frame[:,:,0]=np.ones((300,300))-frame[:,:,1]-frame[:,:,2]
#Only keep lower triangle, where the Blue component is not negative:
#print(frame.shape)
frame[:,:,2]=np.tril(frame[:,:,2])
frame[:,:,1]=np.tril(frame[:,:,1])
frame[:,:,0]=np.tril(frame[:,:,0])
#lower left Pixel, 1 to the right:
print('Lower left Pixel:',frame[299,0,:])
#upper left Pixel:
print('Upper left Pixel:',frame[0,0,:])
#Lower right Pixel:
print('Lower right Pixel:',frame[299,299,:])

# Display the resulting color triangle
cv2.imshow('Color trinagle of possible display colors',frame)
#tri=plt.imshow(frame)
#tri.canvas.set_window_title('Color Triangel, B=1-R-G')
#tri.set_xlabel([0,1])
#tri.set_ylabel([0,1])
#plt.show()

while(True):
   if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, close windows

cv2.destroyAllWindows()

