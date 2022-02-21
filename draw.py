from pickletools import uint8
import cv2 as cv
import numpy as np

#Drawing shapes on images
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#First: Paint the image with Certain Colour
#blank[:] = 0,0,255 #red colour

#Second: Drawing a shape like Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=2)

cv.imshow('Rectangle', blank)

#3Drawing a Circle
cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 40,(0,0,255), thickness=-1)
cv.imshow('Circle', blank)

#4Drawing a line
cv.line(blank, (0,0),  (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=2)
cv.imshow('Line', blank)

#5 Writing text
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)


blank[:] = 0,0,255 #portion into a red colour
cv.imshow('Red', blank)

cv.waitKey(0)
 