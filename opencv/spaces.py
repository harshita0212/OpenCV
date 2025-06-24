import cv2 as cv
import matplotlib.pyplot as plt
 #color sapces : a system representing an array of pixel color:
 #rgb, pixel

img = cv.imread('photos/abc.jpg')
cv.imshow('Cat', img)

plt.imshow(img)
plt.show()


# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#bgr to hsv

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#bgr to lab
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# plt.imshow(rgb)
# plt.show()

#lab to bgr
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)


cv.waitKey(0)
