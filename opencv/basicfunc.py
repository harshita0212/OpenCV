import cv2 as cv

img = cv.imread('photos/abc.jpg')

cv.imshow('Cat', img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#how to blur an image - reduce noise
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#edge cascade - edges in an image

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

#dilating the image- canny image with edges
dilated = cv.dilate(canny, (7,7),iterations=3)
cv.imshow('dilated image', dilated)


#eroding
eroded = cv.erode(dilated, (7,7),iterations=3)
cv.imshow('eroded image', eroded)

#resize and crop

resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)


cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)