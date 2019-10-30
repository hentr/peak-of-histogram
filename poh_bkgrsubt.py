"""
    This is a peak-of-histogram background subtraction algorithm using numpy. It is suitable for dark-field microscopy data, though was developed specifically for dark-field scanning transmission electron microscopy images (STEM), but is likely useful for lots of other images as well. 
    
    Author: Trond Henninen, trond.henninen@empa.ch
    
    The background substraction has two modes:
        (default) individual_frames=True - subtracts the peak of the histogram from each frame of the image stack individually (best preserves quantitative constrast for data with a changing background)
        individual_frames=False - subtracts the peak of the histogram from the entire of the image stack altogether (best preserves quantitative constrast for data with a static background)
    
    This code reads/writes most common image formats (including tifimage stacks) using scikit-image, which can be installed using pip or conda:
        $ pip install scikit-image
        $ conda install scikit-image -c conda-forge
    
    In addition almost all electron microscopy data can be read by hyperspy, which can be installed using pip or conda: 
        $ pip install hyperspy
        $ conda install hyperspy -c conda-forge
        
    If using hyperspy,  uncomment line 24 and replace lines 62-63 with 65-67
"""

from numpy import argmax, histogram, zeros
import os, glob
from skimage import io
#from hyperspy.api import load


def bkgrsubt(imgdata,individual_frames=True):
    nbins = 100 #number of bins for the histogram, 100 should be precise enough
    if len(imgdata.shape) == 2: individual_frames=False
    
    if individual_frames == False: #removes image background from peak of the entire image series' histogram
        h = histogram(imgdata,bins=nbins)
        hmax = h[1][argmax(h[0])]
        subimg = imgdata-hmax
        subimg[subimg < 1] = 1 #set negative and 0 values to 1 to avoid divide-by-zero errors in later processing
        return(subimg)
        
    elif individual_frames == True: #removes image background from each frame individually, using peak of the image's histogram
        newstack = zeros(imgdata.shape)
        for i,img in enumerate(imgdata):
            h = histogram(img,bins=nbins)
            hmax = h[1][argmax(h[0][1:])]  # max of the histogram (ignoring the first bin of the histogram, e.g. black pixels)
            subimg = img-hmax
            subimg[subimg < 1] = 1  #set negative and 0 values to 1 to avoid divide-by-zero errors in later processing
            newstack[i,:,:] = subimg
        return(newstack)
    else:
        raise('"individual_frames" must be True or False')


if __name__ == '__main__':  
    filetype = 'tif'    #choose which filetype to apply the background subtraction
    dir = r'path to folder with files'

    os.chdir(dir)
    files = glob.glob('*.'+filetype)      
    print(files)
    for file in files:
        name = os.path.splitext(os.path.basename(file))[0] #filename without the file extension
        
        #if using hyperspy, replace the following two lines with the last three lines
        imgs = io.imread(file)
        io.imsave(name+'_bkgrsubt.tif',bkgrsubt(imgs,individual_frames=True).astype('uint16'))

        #s = load(file)
        #s.data = bkgrsubt(s.data,individual_frames=True).astype('uint16')
        #s.save(name+'_bkgrsubt.tif', overwrite=True)
