import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("../images/land.jpg")
cv.imshow("img",img)

#masking
blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("blank",blank)

#drawing line
line = cv.line(blank, (70,0),(100,70),(255,0,255), thickness=1)
cv.imshow("line",line)

#drawing shapes
#1. rectangle
rectangle = cv.rectangle(blank, (10,140),(50, 180), (255,255,255), thickness=2)
cv.imshow("rectangle",rectangle)

#2. Circle
circle=cv.circle(blank, (25,50), 25, (255,234,23),thickness=2)
cv.imshow("circle",circle)

#3. Ellipse
Ellipse = cv.ellipse(blank, (100,100),(40,60), 30, 0, 360, (255, 0, 0), 2)
cv.imshow("Ellipse",Ellipse)


cv.waitKey(0)
cv.destroyAllWindows()