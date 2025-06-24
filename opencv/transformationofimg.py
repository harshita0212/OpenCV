import cv2 as cv
import numpy as np

img = cv.imread('photos/19870.jpg')

cv.imshow('Friends', img)

#translation - shifting the image to  all dimensions

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x -->> left
# -y -->> up
# x -->> right
# y -->> down

translated = translate(img, 100,100)
cv.imshow('Translated', translated)

translated = translate(img, -100,-100)
cv.imshow('Translated', translated)

# rotation

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None: #rotate from center if no rotation point
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions =(width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)


#flipping

flip = cv.flip(img, 0)
cv.imshow('Flip', flip)



cv.waitKey(0)