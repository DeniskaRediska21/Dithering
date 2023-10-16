from PIL import Image
import numpy as np


def bayer_dither(PATH = '',num_colors = 2,kernel_size = 2,scale_factor = 1,Binary_dithering = True, Grayscale = False,verbose = True ,IMAGE = None):
    if IMAGE is None:
        img = np.array(Image.open(PATH))/255
    else:
        img = np.array(IMAGE)/255

    if kernel_size == 2:
        M = np.array([[0,2],[3,1]]) / np.power(kernel_size,2) - 0.5
    elif kernel_size==4:
        M = np.array([[0,8,2,10],[12,4,14,6],[3,11,1,9],[15,7,13,5]]) / np.power(kernel_size,2) - 0.5
    elif kernel_size==8: 
        M = np.array([[0,32,8,40,2,34,10,42],[48,16,56,24,50,18,58,26],[12,44,4,36,14,46,6,38],[60,28,52,20,62,30,54,22],[3,35,11,43,1,33,9,41],[51,19,59,27,49,17,57,25],[15,47,7,39,13,45,5,37],[63,31,55,23,61,29,53,21]]) / np.power(kernel_size,2) - 0.5
            
    if Grayscale:
        img = np.mean(img,axis = 2)
        
    img_quantised = np.floor(img*(num_colors-1)+0.5)/(num_colors-1)

    M = np.tile(M,(img.shape[0]//kernel_size,img.shape[1]//kernel_size))[0:img.shape[0],0:img.shape[1],None]

    if np.size(img_quantised.shape) < 3:    
        img_quantised = img_quantised[:,:,None]
        
    if Binary_dithering:
        img_quantised[img_quantised<M] = 0
        img_quantised[img_quantised>M] = 1
    else:
        img_quantised += scale_factor*M


    if img_quantised.shape[2]==1:
        img_quantised = np.squeeze(img_quantised)


    img_quantised = Image.fromarray((img_quantised*255).astype(np.uint8))

    if verbose:
        img_quantised.show()

    return img_quantised



# img = bayer_dither('Data/Penguins.jpg',num_colors = 2,kernel_size = 2,scale_factor = 0.1,Binary_dithering = False,Grayscale = False,verbose = True)
# img.save("Results/bayer_full_color_additive.jpg")
# 
# img = bayer_dither('Data/Penguins.jpg',num_colors = 2,kernel_size = 2,scale_factor = 0.1,Binary_dithering = True,Grayscale = True,verbose = True)
# img.save("Results/bayer_binary.jpg")

