# pip install opencv-contrib-python
import cv2
import numpy as np

# Read image
plane = r'C:\Users\MOHAMMAD AKRAMA\OneDrive\Pictures\Camera Roll\Camera\.trashed-1663996063-IMG20220825103701.jpg'
img = cv2.imread(plane)
if img is None:
    print('Could not open or find the image:', plane)
    exit(0)
print('type', type(img))
print('shape', img.shape)

# resize image by width and height
img_100= cv2.resize(img, (100, 50))
# resize image by scale
# img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

# filters - grayscale, edge detection, bgrtorgb
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_egde = cv2.Canny(img, 100, 200) # 100, 200 are threshold values


# Display image
cv2.imshow('image gray', img_gray)
cv2.imshow('image rgb', img_rgb)
cv2.imshow('image', img)
cv2.imshow('image edge', img_egde)

cv2.waitKey(0) # waits until a key is pressed