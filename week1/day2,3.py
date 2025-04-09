import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../images/redd.jpg")
cv.imshow("img",img)

# Resizing
resize = cv.resize(img,None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
cv.imshow("resized image",resize)

#Flipping
flip = cv.flip(img, 0)    #0-vertical; 1-horizontal, -1- 180 degree
cv.imshow("flipped", flip)

#Rotating
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle,1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated=rotate(img, 90)
rotate_rotate=rotate(rotated, -125)
cv.imshow("rotated90", rotated)
cv.imshow("rotated35", rotate_rotate)

#cropping
image = cv.imread("../images/land.jpg")
crop = image[50:100, 20:60]
cv.imshow("cropped image", crop)

cv.waitKey(0)
cv.destroyAllWindows()


