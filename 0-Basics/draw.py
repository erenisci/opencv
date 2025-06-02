import cv2 as cv
import numpy as np

# Create blank image
# blank = np.zeros((500, 500), dtype='uint8')
# cv.imshow('Blank', blank)

# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)

# cv.waitKey(0)


# Paint the image a certain color
blank = np.zeros((500, 500, 3), dtype='uint8')

# Paint the image green
# blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

# Paint the given area to the red
blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Red square', blank)

# Write text in an image
cv.putText(blank, 'Hello', (200, 300),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
