import os
import cv2 as cv
import numpy as np

people = ['ambani', 'amitabh bacchan', 'elon musk','ratan tata']
DIR = r'C:\Users\harsh\Downloads\faces'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features =[]
labels =[]

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)
            
            for(x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

# print(f'Length of the features = {len(features)}')
# print(f'Length of the labels = {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecgnizer_create()

#train the recognizer on the features and labels list





# p = []
# for i in os.listdir(r'C:\Users\harsh\Downloads\faces'):
#     p.append(i)

# print(p)




    