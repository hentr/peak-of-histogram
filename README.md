# peak-of-histogram
This is a peak-of-histogram image background subtraction algorithm using numpy/python. It calculates the histogram and subtracts the peak value from the image. It is suitable for dark-field microscopy data, though was developed specifically for dark-field scanning transmission electron microscopy images (STEM), but is likely useful for lots of other images as well.
    
Author: Trond Henninen, trond.henninen@empa.ch
       
This code reads/writes most common image formats (including tif image stacks) using scikit-image, which can be installed using pip or conda:

> pip install scikit-image

> conda install scikit-image -c conda-forge


    
In addition almost all electron microscopy data can be read by hyperspy, which can be installed using pip or conda: 

> pip install hyperspy

> conda install hyperspy -c conda-forge
