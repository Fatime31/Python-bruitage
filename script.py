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
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            voisinage = []
            for x2 in range(x-rayon,x+rayon+1,1):
                for y2 in range(y-rayon,y+rayon+1,1):
                    if (x2 >= 0 and y2 >= 0 and x2 < image.shape[0] and y2 < image.shape[1]):
                        voisinage.append(image[x2,y2])
            image[x,y] = stat.mean(voisinage)
    return image

def filtrageMedian(rayon, image):
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            voisinage = []
            for x2 in range(x-rayon,x+rayon+1,1):
                for y2 in range(y-rayon,y+rayon+1,1):
                    if (x2 >= 0 and y2 >= 0 and x2 < image.shape[0] and y2 < image.shape[1]):
                        voisinage.append(image[x2,y2])
            image[x,y] = stat.median(voisinage)
    return image

#------------------------------------------------------------------------------

img="Reference_pour_SNR/dcode-image.png"
img2="Reference_pour_SNR/image1_reference.png"

image = io.imread(img)

#io.imshow(filtrageMedian(1,saltPepper(0.1, image)))

#io.imshow(bruitAdditif(20, image))
#io.imshow(filtrageConvolution(1,bruitAdditif(20, image)))

#io.imshow(bruitMultiplicatif(0.3, image))


