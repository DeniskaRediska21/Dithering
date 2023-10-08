from PIL import Image
import numpy as np
from scipy.ndimage.filters import gaussian_filter


img = np.array(Image.open('Data/Penguins.jpg'))/255


Grayscale = True

n = 4
     
if Grayscale:
    img = np.mean(img,axis = 2)
    
img_quantised = img

if np.size(img_quantised.shape) < 3:    
    img_quantised = img_quantised[:,:,None]
    
h = img_quantised.shape[0]
l = img_quantised.shape[1]
for c in range(img_quantised.shape[2]):    
    for row in range(h):
        for column in range(l):
            old_c = img_quantised[row,column,c]
            img_quantised[row,column,c] = np.floor(img_quantised[row,column,c]*(n-1)+0.5)/(n-1)
            err = old_c - img_quantised[row,column,c]
            if row < h-1:
                img_quantised[row+1,column,c] += err/2
            if column < l-1:
                img_quantised[row,column+1,c] += err/2
        


if img_quantised.shape[2]==1:
    img_quantised = np.squeeze(img_quantised)


img_quantised = Image.fromarray((img_quantised*255).astype(np.uint8))
img_quantised.show()

