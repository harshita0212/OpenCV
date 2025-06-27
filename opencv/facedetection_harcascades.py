#haar cascades - open cv built in classifier to detect face
import cv2 as cv

img = cv.imread('photos/16445.jpg')
cv.imshow('Person', img)

#face detection does not involve skin tone or the  colors in the image

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

#rectangular coordinates for the faces present in the image 
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)

print(f'Number of faces found= {len(faces_rect)}')


#will detect the faces in the image- will also mark the neck or other skin showing areas, as 
#haar cascades are really sensitive to noise 
#try changing image and try - by changing the thickness we can detect more faces
for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness =2)

cv.imshow('Detected image',img)


cv.waitKey(0)
