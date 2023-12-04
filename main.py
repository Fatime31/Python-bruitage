import toolimages as ti 
from skimage import  io
import pandas as pd

images = ['Reference_pour_SNR/image1_reference.png','Reference_pour_SNR/image2_reference.png',
          'Reference_pour_SNR/dcode-image.png']

for img in images:
    imgname = img.split(".")[0]
    image = io.imread(img)
    io.imsave(imgname+"Salt01.png",ti.saltPepper(0.1, image))
    image = io.imread(img)
    io.imsave(imgname+"Add35.png",ti.bruitAdditif(35,image))
    image = io.imread(img)
    io.imsave(imgname+"Mult03.png",ti.bruitMultiplicatif(0.3,image))
    image = io.imread(img)
    imgBord = ti.detectionBord(image)

    modifiedImages = [imgname+"Salt01.png",imgname+"Add35.png",imgname+"Mult03.png"]
    for mimg in modifiedImages:
        mimgname = mimg.split(".")[0]
        mimage = io.imread(mimg)
        io.imsave(mimgname+"_Conv.png",ti.filtrageConvolution(1,mimage))
        mimage = io.imread(mimg)
        io.imsave(mimgname+"_Conv2.png",ti.filtrageConvolution(2,mimage))
        mimage = io.imread(mimg)
        io.imsave(mimgname+"_ConvDB.png",ti.filtrageConvolutionDB(1,mimage,imgBord))
        mimage = io.imread(mimg)
        io.imsave(mimgname+"_Conv2DB.png",ti.filtrageConvolutionDB(2,mimage,imgBord))
        mimage = io.imread(mimg)
        pond1 = [1,2,1,2,4,2,1,2,1]
        io.imsave(mimgname+"_Pond.png",ti.filtrageConvolutionPondere(1,mimage,pond1))
        mimage = io.imread(mimg)
        pond2 = [1,4,6,4,1,4,16,24,16,4,6,24,36,24,6,4,16,24,16,4,1,4,6,4,1]
        io.imsave(mimgname+"_Pond2.png",ti.filtrageConvolutionPondere(2,mimage,pond2))
        mimage = io.imread(mimg)
        io.imsave(mimgname+"_PondDB.png",ti.filtrageConvolutionPondereDB(1,mimage,pond1,imgBord))
        mimage = io.imread(mimg)
        io.imsave(mimgname+"_Pond2DB.png",ti.filtrageConvolutionPondereDB(2,mimage,pond2,imgBord))
        mimage = io.imread(mimg)
        io.imsave(mimgname+"_Med.png",ti.filtrageMedian(1,mimage))
        mimage = io.imread(mimg)
        io.imsave(mimgname+"_Med2.png",ti.filtrageMedian(2,mimage))
        mimage = io.imread(mimg)
        io.imsave(mimgname+"_MedDB.png",ti.filtrageMedianDB(1,mimage,imgBord))
        mimage = io.imread(mimg)
        io.imsave(mimgname+"_Med2DB.png",ti.filtrageMedianDB(2,mimage,imgBord))
        

bruite = ["Salt01.png","Add35.png","Mult03.png"]
debruite = ["_Conv.png","_Conv2.png","_ConvDB.png","_Conv2DB.png",
            "_Pond.png","_Pond2.png","_PondDB.png","_Pond2DB.png",
            "_Med.png","_Med2.png","_MedDB.png","_Med2DB.png"]
result = []
for img in images:
    imgOriginal = io.imread(img)
    imgname = img.split(".")[0]
    for b in bruite:
        t = [imgname.split("/")[-1],b.split(".")[0]]
        imgBruite = io.imread(imgname+b)
        t.append(ti.SNR(imgOriginal, imgBruite))
        imgbname = (imgname+b).split(".")[0]
        for db in debruite:
            imgBruite = io.imread(imgbname+db)
            t.append(ti.SNR(imgOriginal, imgBruite))
        result.append(t)

Datas = pd.DataFrame(data=result,
                     columns=['Image de depart','type de bruitage','SNR bruité',
                              'Conv','Conv 2','Conv DB','Conv 2 DB',
                              'Pond','Pond 2','Pond DB','Pond 2 DB',
                              'Med','Med 2','Med DB','Med 2 DB'])

Datas.to_excel('./SNR_Tab.xlsx')