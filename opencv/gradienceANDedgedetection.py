#2 ways to compute edges

import cv2 as cv
import numpy as np

img = cv.imread('photos/19870.jpg')
cv.imshow('Friends', img)


# blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', blank)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#laplacian - PENCIL SHADING OF THE IMAGE - edges

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplaciaan', lap)

#sobel - gradience in the x and the y direction
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)


cv.waitKey(0)
