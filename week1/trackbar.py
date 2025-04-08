#week 1 day 2 image resizing mini project 1: TRACKBAR
#MiniProject1

import cv2 as cv
def nothing(x):
    pass
img = cv.imread("../images/girl.jpeg")
cv.namedWindow("img")
cv.createTrackbar("Scale X", "img",200,400,nothing)
cv.createTrackbar("Scale Y", "img",200,400,nothing)
while True:
    fx = cv.getTrackbarPos("Scale X","img")/100
    fy = cv.getTrackbarPos("Scale Y","img")/100
    if fx==0 or fy==0:
        cv.waitKey(1)
        continue
    resized = cv.resize(img, None, fx=fx, fy=fy, interpolation=cv.INTER_CUBIC )
    cv.imshow("img",resized)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()