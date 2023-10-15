from PIL import Image
import numpy as np

def white_noise_dither(PATH, num_colors = 2, scale_factor = 0.1, Binary_dithering = True, Grayscale = True):
    img = np.array(Image.open(PATH))/255
    M = np.abs(np.random.randn(img.shape[0],img.shape[1])[:,:,None])

    if Grayscale:
        img = np.mean(img,axis = 2)
        
    img_quantised = np.floor(img*(num_colors-1)+0.5)/(num_colors-1)

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
    img_quantised.show()
    return img_quantised

# img = white_noise_dither('Data/Penguins.jpg', num_colors = 2, scale_factor = 0.1, Binary_dithering = True, Grayscale = True)
# img.save('Results/white_noise_dither_grayscale.jpg')
# 
# img = white_noise_dither('Data/Penguins.jpg', num_colors = 2, scale_factor = 0.1, Binary_dithering = True, Grayscale = False)
# img.save('Results/white_noise_dither_full_color.jpg')
