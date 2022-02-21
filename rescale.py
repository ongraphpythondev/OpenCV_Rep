#Resizing and Rescaling Images in OpenCV
import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)


def rescaleFrame(frame, scale=0.75):
    #This method works well for images, Video and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#resizing Images using Above function
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)


def changeRes(width, height):
    #Live Video Only not work on Static images and videos
    capture.set(3, width)
    capture.set(4,height)

#Reading videos in opencv
capture = cv.VideoCapture('Videos/dog.mp4')

while True: 
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, 0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
