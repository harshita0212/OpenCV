import cv2 as cv
import numpy as np

img = cv.imread('photos/abc.jpg')
cv.imshow('Photos', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', mask)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird_shape', weird_shape)





masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked) #intersecting two images one on top of another





cv.waitKey(0)