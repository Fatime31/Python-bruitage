#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:15:25 2023

@author: ndiayefatime
"""
from skimage import  io
import statistics as stat
import numpy as np
import random

def saltPepper(niveauBruit,image):
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            rand = random.random()
            if(rand<(niveauBruit/2)):
                image[x,y]=0
            elif(rand>1-(niveauBruit/2)):
                image[x,y]=255
    return image

def bruitAdditif(niveauBruit,image):
    bruit = np.random.randn(image.shape[0],image.shape[1])
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x,y] = min(max(image[x,y]+(bruit[x,y]*niveauBruit),0),255)
    return image

def bruitMultiplicatif(niveauBruit,image):
    bruit = np.random.randn(image.shape[0],image.shape[1])
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x,y] = min(max(image[x,y]*(1+(bruit[x,y]*niveauBruit)),0),255)
    return image

def filtrageConvolution(rayon, image):
    image = np.double(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            voisinage = []
            for x2 in range(x-rayon,x+rayon+1,1):
                for y2 in range(y-rayon,y+rayon+1,1):
                    if (x2 >= 0 and y2 >= 0 and x2 < image.shape[0] and y2 < image.shape[1]):
                        voisinage.append(image[x2,y2])
            image[x,y] = stat.mean(voisinage)
    image = np.ubyte(image)
    return image

def filtrageMedian(rayon, image):
    image = np.double(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            voisinage = []
            for x2 in range(x-rayon,x+rayon+1,1):
                for y2 in range(y-rayon,y+rayon+1,1):
                    if (x2 >= 0 and y2 >= 0 and x2 < image.shape[0] and y2 < image.shape[1]):
                        voisinage.append(image[x2,y2])
            image[x,y] = stat.median(voisinage)
    image = np.ubyte(image)
    return image

#------------------------------------------------------------------------------

img="Reference_pour_SNR/image2_reference.png"

image = io.imread(img)
io.imsave("Reference_pour_SNR/img2Salt01.png",saltPepper(0.1, image))
image = io.imread(img)
io.imsave("Reference_pour_SNR/img2Add35.png",bruitAdditif(35,image))
image = io.imread(img)
io.imsave("Reference_pour_SNR/img2Mult03.png",bruitMultiplicatif(0.3,image))

img1="Reference_pour_SNR/img2Salt01.png"
img2="Reference_pour_SNR/img2Add35.png"
img3="Reference_pour_SNR/img2Mult03.png"

image1 = io.imread(img1)
io.imsave("Reference_pour_SNR/img2Salt01_Conv.png",filtrageConvolution(1,image1))
image1 = io.imread(img1)
io.imsave("Reference_pour_SNR/img2Salt01_Conv2.png",filtrageConvolution(2,image1))
image1 = io.imread(img1)
io.imsave("Reference_pour_SNR/img2Salt01_Med.png",filtrageMedian(1,image1))
image1 = io.imread(img1)
io.imsave("Reference_pour_SNR/img2Salt01_Med2.png",filtrageMedian(2,image1))

image2 = io.imread(img2)
io.imsave("Reference_pour_SNR/img2Add35_Conv.png",filtrageConvolution(1,image2))
image2 = io.imread(img2)
io.imsave("Reference_pour_SNR/img2Add35_Conv2.png",filtrageConvolution(2,image2))
image2 = io.imread(img2)
io.imsave("Reference_pour_SNR/img2Add35_Med.png",filtrageMedian(1,image2))
image2 = io.imread(img2)
io.imsave("Reference_pour_SNR/img2Add35_Med2.png",filtrageMedian(2,image2))

image3 = io.imread(img3)
io.imsave("Reference_pour_SNR/img2Mult03_Conv.png",filtrageConvolution(1,image3))
image3 = io.imread(img3)
io.imsave("Reference_pour_SNR/img2Mult03_Conv2.png",filtrageConvolution(2,image3))
image3 = io.imread(img3)
io.imsave("Reference_pour_SNR/img2Mult03_Med.png",filtrageMedian(1,image3))
image3 = io.imread(img3)
io.imsave("Reference_pour_SNR/img2Mult03_Med2.png",filtrageMedian(2,image3))