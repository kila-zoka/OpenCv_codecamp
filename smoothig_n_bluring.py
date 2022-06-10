from random import gauss
from statistics import median
import cv2 as cv
from cv2 import imread
from cv2 import bilateralFilter


img = cv.imread('images/reimg.png')

# averaging

avg = cv.blur(img, (3, 3))
cv.imshow('averaging', avg)

# gaussian blur

gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gauss)

# median blur

media = cv.medianBlur(img, 3)
cv.imshow('Median Blur', media)

# bilateral bluring

bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
