import cv2 as cv
import numpy as np

img = cv.imread('photos/19870.jpg')
cv.imshow('Friends', img)

#splitting the image into its three colour channels

b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


cv.waitKey(0)