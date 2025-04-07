import cv2 as cv
img = cv.imread("../images/redd.jpg")  #for reading the image
cv.imshow("img",img)  # for displaying the image


# COLOR SPACES

# 1. BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# 2. BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# 3. BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# 4. BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# 5. BGR to HLS
hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)
cv.imshow("HLS", hls)

# 6. HLS to BGR
hlsx = cv.cvtColor(hls, cv.COLOR_HLS2BGR)
cv.imshow("HLSX", hlsx)

# 7. LAB to BGR
labx = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("LABX", labx)

# 8. RGB to BGR
rgbx = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow("RGBX", rgbx)

# 9. HSV to BGR
hsvx = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSVX", hsvx)

# 10. Grayscale to BGR 
grayx = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow("grayx",grayx)

cv.waitKey(0)
cv.destroyAllWindows()