from tokenize import blank_re
import cv2 as cv
import numpy as np

img = cv.imread('images/reimg.png')
cv.imshow('img', img)


blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)


blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


cv.imshow('b', blue)
cv.imshow('g', green)
cv.imshow('r', red)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged_img = cv.merge([b, g, r])
cv.imshow('img merge', merged_img)

cv.waitKey(0)
