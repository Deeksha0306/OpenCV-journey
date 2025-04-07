import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("../images/girl.jpeg")
cv.imshow("img", img)
# Resize image
resize = cv.resize(img,None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
cv.imshow("resized image",resize)


cv.waitKey(0)
cv.destroyAllWindows()