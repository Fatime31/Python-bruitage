#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:15:25 2023

@author: ndiayefatime
"""
from skimage import  io
import random

def saltPepper(niveauBruit,imagePath):
    image = io.imread(imagePath)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            rand = random.random()
            if(rand<(niveauBruit/2)):
                image[x,y]=0
            elif(rand>1-(niveauBruit/2)):
                image[x,y]=255
    return image



img="Reference_pour_SNR/image1_reference.png"



io.imshow(saltPepper(0.1,img))

