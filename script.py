#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:15:25 2023

@author: ndiayefatime
"""
from skimage import  io
from skimage.color import rgb2gray
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



img="Reference_pour_SNR/dcode-image.png"

image = io.imread(img)

#io.imshow(saltPepper(0.1, image))

#io.imshow(bruitAdditif(20, image))

io.imshow(bruitMultiplicatif(0.3, image))
