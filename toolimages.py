import statistics as stat
import numpy as np
import random

#------------------------------ BRUITAGE --------------------------------------
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

#----------------------------- DEBRUITAGE -------------------------------------
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

def filtrageConvolutionPondere(rayon, image, ponderation):
    image = np.double(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            voisinage = []
            for x2 in range(x-rayon,x+rayon+1,1):
                for y2 in range(y-rayon,y+rayon+1,1):
                    if (x2 >= 0 and y2 >= 0 and x2 < image.shape[0] and y2 < image.shape[1]):
                        voisinage.append(image[x2,y2])
                    else:
                        voisinage.append(-1)
            image[x,y] = moyenPondereMatriciel(voisinage,ponderation)
    image = np.ubyte(image)
    return image

def moyenPondereMatriciel(matrice, ponderation):
    total = 0 
    pond = 0
    for x in range(len(matrice)):
        if (matrice[x] >= 0):
            total += matrice[x]*ponderation[x]
            pond += ponderation[x]
    return total/pond

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

def detectionBord(image):
    MasqueDeDerivationX = [-1,0,1,-2,0,2,-1,0,1]
    MasqueDeDerivationY = [-1,-2,-1,0,0,0,1,2,1]
    image = np.double(image)
    imageContour = np.zeros((image.shape[0],image.shape[1]))
    for x in range(1,image.shape[0]-1):
        for y in range(1,image.shape[1]-1):
            voisinage = []
            for x2 in range(x-1,x+2,1):
                for y2 in range(y-1,y+2,1):
                    if (x2 >= 0 and y2 >= 0 and x2 < image.shape[0] and y2 < image.shape[1]):
                        voisinage.append(image[x2,y2])
            Gx = 0 
            Gy = 0
            for k in range(9):
                Gx += (voisinage[k]*MasqueDeDerivationX[k])
                Gy += (voisinage[k]*MasqueDeDerivationY[k])
            imageContour[x,y] = np.sqrt(Gx**2+Gy**2)
    imageContour = np.ubyte(imageContour)
    return imageContour

def filtrageConvolutionDB(rayon, image, imgBord):
    image = np.double(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if (imgBord[x,y]<100):
                voisinage = []
                for x2 in range(x-rayon,x+rayon+1,1):
                    for y2 in range(y-rayon,y+rayon+1,1):
                        if (x2 >= 0 and y2 >= 0 and x2 < image.shape[0] and y2 < image.shape[1]):
                            voisinage.append(image[x2,y2])
                image[x,y] = stat.mean(voisinage)
    image = np.ubyte(image)
    return image

def filtrageConvolutionPondereDB(rayon, image, ponderation, imgBord):
    image = np.double(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if (imgBord[x,y]<100):
                voisinage = []
                for x2 in range(x-rayon,x+rayon+1,1):
                    for y2 in range(y-rayon,y+rayon+1,1):
                        if (x2 >= 0 and y2 >= 0 and x2 < image.shape[0] and y2 < image.shape[1]):
                            voisinage.append(image[x2,y2])
                        else:
                            voisinage.append(-1)
                image[x,y] = moyenPondereMatriciel(voisinage,ponderation)
    image = np.ubyte(image)
    return image

def filtrageMedianDB(rayon, image, imgBord):
    image = np.double(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if (imgBord[x,y]<100):
                voisinage = []
                for x2 in range(x-rayon,x+rayon+1,1):
                    for y2 in range(y-rayon,y+rayon+1,1):
                        if (x2 >= 0 and y2 >= 0 and x2 < image.shape[0] and y2 < image.shape[1]):
                            voisinage.append(image[x2,y2])
                image[x,y] = stat.median(voisinage)
    image = np.ubyte(image)
    return image

#--------------------------------- SNR ----------------------------------------
def PSignal(imageBruit):
    img = np.single(imageBruit)
    somme = 0
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            somme +=img[x,y]**2
    return somme
        
def PBruit(imageR,imageBruit):
    imgReference = np.single(imageR)
    imgBruit = np.single(imageBruit)
    somme = 0
    for x in range(imgReference.shape[0]):
        for y in range(imgReference.shape[1]):
            somme += (imgReference[x,y]- imgBruit[x,y])**2
    return somme

def SNR (image,imageBruit):
    return 10 * np.log10(PSignal(imageBruit)/PBruit(image,imageBruit))