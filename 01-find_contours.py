#!/usr/bin/python3

import cv2

# read img and get a copy 
img = cv2.imread("source/mountain.jpeg")
img_copy = img.copy()

# remove color
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) 
# find canny
canny = cv2.Canny(gray_img, 150, 200)
# find contours, it will return herarchy as well, but it is ignored.
contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    cv2.drawContours(img_copy, cnt, -1, (255, 0, 0), 2)
    # print area of contour
    print(f'Area of contour is {cv2.contourArea(cnt)}') 
    # check the counter vertice
    cnt_len = cv2.arcLength(cnt, True)
    vertice = cv2.approxPolyDP(cnt, cnt_len * 0.02, True)
    corners = len(vertice)
    print(f'Number of vertice is: {corners}')
    # find a bounding box
    x, y, w, h = cv2.boundingRect(vertice)
    cv2.rectangle(img_copy, (x,y), (x+w, y+h), (0, 255, 0), 2)

# show orignal img
cv2.imshow('img', img)
# show img countours
cv2.imshow('img_contour', img_copy)
cv2.waitKey(0)