import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (3, 3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gaussian)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
