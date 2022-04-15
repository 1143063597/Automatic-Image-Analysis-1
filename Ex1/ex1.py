#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Simon Matern
"""

import numpy as np
import cv2 as cv
import utils


def binarizeImage(img, thresh):
    """
    Given a coloured image and a threshold binarizes the image.
    Values below thresh are set to 0. All other values are set to 255
    """
    tempImg = img.copy()
    gray_image = cv.cvtColor(tempImg, cv.COLOR_BGR2GRAY)
    gray_image = np.where(gray_image >= thresh, 255, 0)

    return gray_image

def smoothImage(img):    
    """
    Given a coloured image apply a blur on the image, e.g. Gaussian blur
    """
    tempImg = img.copy()

    gaussian_kernel = np.ones((11,11), np.float32) / 121
    res = cv.filter2D(tempImg, -1, gaussian_kernel)
    return res

def doSomething(img):
    """
    Given a coloured image apply any image manipulation. Be creative!
    """
    tempImg = smoothImage(img.copy())
    
    sobelx = cv.Sobel(src=tempImg, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
    
    return sobelx


def processImage(img):
    """
    Given an coloured image applies the implemented smoothing and binarization.
    """
    img = smoothImage(img)
    img = binarizeImage(img, 125)
    return img


if __name__=="__main__":
    img = cv.imread("test.jpg")
    utils.show(img)
    
    img1 = smoothImage(img)
    utils.show(img1)
    cv.imwrite("result1.jpg", img1)
    
    img2 = binarizeImage(img, 125)
    utils.show(img2)
    cv.imwrite("result2.jpg", img2)
   
    img3 = processImage(img)
    utils.show(img3)
    cv.imwrite("result3.jpg", img3)
    
    img4 = doSomething(img)
    utils.show(img4)
    cv.imwrite("result4.jpg", img4)
