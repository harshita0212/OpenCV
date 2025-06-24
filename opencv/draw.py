import cv2 as cv
import numpy as np

# Create a black image: height=500, width=500, 3 channels (BGR)
blank = np.zeros((500, 500, 3), dtype=np.uint8)

# Example drawing: red rectangle
# cv.rectangle(blank, (50, 50), (450, 450), (0, 0, 255), thickness=3)

# Display the image
cv.imshow('Blank Image', blank)


# 1. paint the image a certain colour
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

#2. to paint certain pizels of the image
blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)

#3. draw a rectangle
cv.rectangle(blank, (0,0), (250,250),(0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

#SCALING THE DIMENSION
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2),(0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank) #rectangle to square

#4. draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness =cv.FILLED)
cv.imshow('Circle', blank)

#5. draw a line

cv.line(blank, (100,250), (300,400), (255,255,255), thickness =3)
cv.imshow('Line', blank)

#6.Text on an image

cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)


cv.waitKey(0)
cv.destroyAllWindows()

