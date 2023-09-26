# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:20:03 2023

@author: leobb
"""
from skimage import io
import numpy as np


def PSignal(imageBruitPath):
    img = np.single((io.imread(imageBruitPath)))
    somme = 0
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            somme +=img[x,y]**2
    return somme
        
def PBruit(imageRPath,imageBruitPath):
    imgReference = np.single(io.imread(imageRPath))
    imgBruit = np.single(io.imread(imageBruitPath))
    somme = 0
    for x in range(imgReference.shape[0]):
        for y in range(imgReference.shape[1]):
            somme += (imgReference[x,y]- imgBruit[x,y])**2
    return somme

def SNR (imagePath,imageBruit):
    return 10 * np.log10(PSignal(imageBruit)/PBruit(imagePath,imageBruit))

#------------------------------------------------------------------------------

print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Salt01.png"))
print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Salt01_Conv.png"))
print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Salt01_Conv2.png"))
print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Salt01_Med.png"))
print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Salt01_Med2.png"))

print("---------------------------------------------------------------------")

print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Add35.png"))
print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Add35_Conv.png"))
print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Add35_Conv2.png"))
print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Add35_Med.png"))
print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Add35_Med2.png"))

print("---------------------------------------------------------------------")

print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Mult03.png"))
print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Mult03_Conv.png"))
print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Mult03_Conv2.png"))
print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Mult03_Med.png"))
print(SNR("Reference_pour_SNR/image2_reference.png","Reference_pour_SNR/img2Mult03_Med2.png"))