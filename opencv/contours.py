import cv2 as cv
import numpy as np

img = cv.imread('photos/19870.jpg')

cv.imshow('Friends', img)


blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)


#hierarchial representation of all contours - all the edges found in the image
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#contour is a list - will give count of contour 
print(f'{len(contours)} contour(s) found!')



#visualise the contour of the image by drawing on it 

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contours Drawn',blank)

cv.waitKey(0)
