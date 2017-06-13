import cv2

#Program to capture an image from a camera and display the pixel value on the screen

cap = cv2.VideoCapture(0)

 # Capture one frame
[ret, frame] = cap.read()

print("image format: ", frame.shape)
print("pixel 0,0: ",frame[0,0,:])

