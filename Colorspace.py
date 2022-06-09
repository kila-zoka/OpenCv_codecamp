from turtle import width
import cv2 as cv
from matplotlib.colors import rgb2hex
import matplotlib.pyplot as plt

pic = cv.imread('images/img.png')
# cv.imshow('Original image', pic)


def rescale(frame, scale=0.2):
    width = int(frame.shape[0] * scale * 2)
    height = int(frame.shape[1] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


img = rescale(pic)
# cv.imshow('Resized image', img)
# cv.imwrite('org_img.png', img)
img2 = cv.imread('org_img.png')

# BGR to Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# gray to rgb

bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('GRAY --> BGR', bgr)

# BGR to RGB

rgb = cv.cvtColor(img2, cv.COLOR_BGR2RGB)

# cv.imshow('rgb', rgb)

plt.imshow(rgb)
plt.show()


cv.waitKey(0)
