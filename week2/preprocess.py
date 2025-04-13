import cv2 as cv
import numpy as np
import matplotlib as plt

img = cv.imread("../images/redd.jpg")
cv.imshow("img", img)

#Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#Gaussian Blur
blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)

#Canny - edge detection
canny1 = cv.Canny(img,10,90)
cv.imshow("Canny1",canny1)
canny2 = cv.Canny(img,200,290)
cv.imshow("Canny2",canny2)

#Erosion
kernel = np.ones((1,1),np.uint8)
erode1 = cv.erode(canny1,kernel,iterations = 1)
cv.imshow("erosion1",erode1)
erode2 = cv.erode(canny2,kernel,iterations = 1)
cv.imshow("erosion2",erode2)

#Dilation
dilate1 = cv.dilate(canny1,kernel,iterations = 1)
cv.imshow("dilation1",dilate1)
dilate2 = cv.dilate(canny2,kernel,iterations = 2)
cv.imshow("dilation2",dilate2)

#resizing
img = cv.imread("../images/girl.jpeg")
cv.imshow("image",img)
imgresi = cv.resize(img,(200,599))
cv.imshow("resized",imgresi)

#drawing 
blank = np.zeros((500,500,3), np.uint8)
rectangle = cv.rectangle(blank, (0,0),(250,250), (255,255,255),thickness=2)
rectangle2 = cv.rectangle(blank, (255,0),(500,500), (255,0,0),thickness=2)
plt.imshow(rectangle2)
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()