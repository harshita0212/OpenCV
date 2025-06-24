import cv2 as cv

# img = cv.imread('photos/16632.jpg')  # Replace with an actual image path
# cv.imshow('family', img)

#rescale 
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[1] * scale)
    dimensions(width,height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    
cv.waitKey(0) #keyboard binding function

#resizing and rescaling frames and images - as opencv cannot display Images with a higher proportion than the desktop

capture = cv.VideoCapture('videos/VIDEO.mp4')
while True:
    isTrue, frame = capture.read()#capturing video frame by frame
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame) #to dispay each frame
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitkey(20) & 0xFF==ord('d'):#to stop from indefinite looping
        break #if letter d is pressed then stop playing the video
    
capture.release()
cv.destroyAllWindows()

# # cv.waitkey(0)



        