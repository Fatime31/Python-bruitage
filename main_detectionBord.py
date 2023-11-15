# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:02:13 2023

@author: leobb
"""

import toolimages as ti 
from skimage import  io


image = io.imread('Reference_pour_SNR/image1_reference.png')

io.imshow(ti.detectionBord(image))
io.show()