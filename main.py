import toolimages as ti 
from skimage import  io
import pandas as pd

images = ['Reference_pour_SNR/image1_reference.png']

for img in images:
    imgname = img.split(".")[0]
    image = io.imread(img)
    io.imsave(imgname+"Salt01.png",ti.saltPepper(0.1, image))
    image = io.imread(img)
    io.imsave(imgname+"Add35.png",ti.bruitAdditif(35,image))
    image = io.imread(img)
    io.imsave(imgname+"Mult03.png",ti.bruitMultiplicatif(0.3,image))

    modifiedImages = [imgname+"Salt01.png",imgname+"Add35.png",imgname+"Mult03.png"]
    for mimg in modifiedImages:
        mimgname = mimg.split(".")[0]
        mimage = io.imread(mimg)
        io.imsave(mimgname+"_Conv.png",ti.filtrageConvolution(1,mimage))
        mimage = io.imread(mimg)
        io.imsave(mimgname+"_Conv2.png",ti.filtrageConvolution(2,mimage))
        mimage = io.imread(mimg)
        io.imsave(mimgname+"_Med.png",ti.filtrageMedian(1,mimage))
        mimage = io.imread(mimg)
        io.imsave(mimgname+"_Med2.png",ti.filtrageMedian(2,mimage))
        

bruite = ["Salt01.png","Add35.png","Mult03.png"]
debruite = ["_Conv.png","_Conv2.png","_Med.png","_Med2.png"]
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
                              'SNR debruité par Conv','SNR debruité par Conv 2',
                              'SNR debruité par Med','SNR debruité par Med 2'])

Datas.to_excel('./SNR_Tab.xlsx')