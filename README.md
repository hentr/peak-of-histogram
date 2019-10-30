# peak-of-histogram
This is a peak-of-histogram background subtraction algorithm using numpy. It is suitable for dark-field microscopy data, though was developed specifically for dark-field scanning transmission electron microscopy images (STEM), but is likely useful for lots of other images as well. 
    
Author: Trond Henninen, trond.henninen@empa.ch
    
The background substraction has two modes:

(default) individual_frames=True - subtracts the peak of the histogram from each frame of the image stack individually (best preserves quantitative constrast for data with a changing background)
    
individual_frames=False - subtracts the peak of the histogram from the entire of the image stack altogether (best preserves quantitative constrast for data with a static background)
    
This code reads/writes most common image formats (including tifimage stacks) using scikit-image, which can be installed using pip or anaconda:

> pip install scikit-image

> conda install scikit-image -c conda-forge
    
In addition almost all electron microscopy data can be read by hyperspy, which can be installed using pip or anaconda: 

> pip install hyperspy

> conda install hyperspy -c conda-forge
