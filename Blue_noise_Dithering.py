from PIL import Image
import numpy as np
from scipy.ndimage.filters import gaussian_filter


img = np.array(Image.open('Data/Penguins.jpg'))/255


Dithering = True
Binary_dithering = True
Grayscale = True

n = 2
s = 1
sigma = 5

M = np.abs(np.random.randn(img.shape[0],img.shape[1])[:,:,None])
M = gaussian_filter(M, sigma)        

if Grayscale:
    img = np.mean(img,axis = 2)
    
img_quantised = np.floor(img*(n-1)+0.5)/(n-1)

if np.size(img_quantised.shape) < 3:    
    img_quantised = img_quantised[:,:,None]
    
if Dithering:
    if Binary_dithering:
        img_quantised[img_quantised<M] = 0
        img_quantised[img_quantised>M] = 1
    else:
        img_quantised += s*M


if img_quantised.shape[2]==1:
    img_quantised = np.squeeze(img_quantised)


img_quantised = Image.fromarray((img_quantised*255).astype(np.uint8))
img_quantised.show()

