from turtle import width
import cv2 as cv

pic = cv.imread('images/img.png')
# cv.imshow('Original image', pic)


def rescale(frame, scale=0.2):
    width = int(frame.shape[0] * scale * 2)
    height = int(frame.shape[1] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


resized_img = rescale(pic)
cv.imshow('Resized image', resized_img)

cv.waitKey(0)
