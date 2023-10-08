from PIL import Image
import numpy as np

img = np.array(Image.open('Data/Lerik.jpg'))/255


Dithering = True
Binary_dithering = True
Grayscale = False

n = 2
N = 2
s = 1

if N == 2:
    M = np.array([[0,2],[3,1]]) / np.power(N,2) - 0.5
elif N==4:
    M = np.array([[0,8,2,10],[12,4,14,6],[3,11,1,9],[15,7,13,5]]) / np.power(N,2) - 0.5
elif N==8: 
    M = np.array([[0,32,8,40,2,34,10,42],[48,16,56,24,50,18,58,26],[12,44,4,36,14,46,6,38],[60,28,52,20,62,30,54,22],[3,35,11,43,1,33,9,41],[51,19,59,27,49,17,57,25],[15,47,7,39,13,45,5,37],[63,31,55,23,61,29,53,21]]) / np.power(N,2) - 0.5
        
if Grayscale:
    img = np.mean(img,axis = 2)
    
img_quantised = np.floor(img*(n-1)+0.5)/(n-1)

M = np.tile(M,(img.shape[0]//N,img.shape[1]//N))[0:img.shape[0],0:img.shape[1],None]

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

