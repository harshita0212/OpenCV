import cv2 as cv

img = cv.imread('photos/abc.jpg')
cv.imshow('Blurred', img)

#averaging - the pixel intensity of any one pixel will be the average of sum of all othe pixels in a window

average = cv.blur(img, (3,3))
cv.imshow('Average blur', average) 
 #gaussian blur is more natural as compared to natural blur
 #but the intensity is low- it gives weight to all

gauss = cv.blur(img, (3,3), 0)
cv.imshow('gaussian blur', gauss) 

#median blur 
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

#bilateral - applies blurring while retaining the edges

bilateral = cv.bilateralFilter(img, 5,15,15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)