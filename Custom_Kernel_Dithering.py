from PIL import Image
import numpy as np

def custom_kernel_dither(PATH,num_colors = 2, Kernel = 'Simple', Grayscale = True, verbose = True):
    img = np.array(Image.open(PATH))/255
    if Grayscale:
        img = np.mean(img,axis = 2)
        
    img_quantised = img
    
    if np.size(img_quantised.shape) < 3:    
        img_quantised = img_quantised[:,:,None]
        
    h = img_quantised.shape[0]
    l = img_quantised.shape[1]
    
    
    if Kernel == 'Simple':
        kernel = [[None, 0.5],[0.5, 0]] # Simple Error Diffusion
    elif Kernel == 'Floyd':
        kernel = np.array([[0, 0, 7],[3,5, 1]])/16 # Floyd-Steinberg
        kernel[0,1] = None # Floyd-Steinberg
    elif Kernel == 'Jarvis':
        kernel = np.array([[0,0,0,7,5],[3,5,7,5,3],[1,3,5,3,1]])/48 # Jarvis-Judice-Ninke
        kernel[0,2] = None  # Jarvis-Judice-Ninke
    elif Kernel == 'Atkinson':
        kernel = np.array([[0,0,1,1],[1,1,1,0],[0,1,0,0]])/8 # Atkinson
        kernel[0,1] = None # Atkinson
    else:
        kernel = Kernel
        
    
    kernel = np.array(kernel)
    offset = np.squeeze(np.where(np.isnan(kernel.astype(float))))
    kh = np.shape(kernel)[0]
    kl = np.shape(kernel)[1]
    kernel[offset[0],offset[1]] = 0
    kernel = kernel.astype(np.float64)
    for c in range(img_quantised.shape[2]):    
        for row in range(h - kh + offset[0]-1):
            for column in range(l - kl + offset[1]-1):
                old_c = img_quantised[row+offset[0],column+offset[1],c]
                img_quantised[row+offset[0],column+offset[1],c] = np.floor(img_quantised[row+offset[0],column+offset[1],c]*(num_colors-1)+0.5)/(num_colors-1)
                err = old_c - img_quantised[row+offset[0],column+offset[1],c]
                img_quantised[row:row+kh,column:column+kl,c] += err*kernel
                
    
    
    if img_quantised.shape[2]==1:
        img_quantised = np.squeeze(img_quantised)
    
    img_quantised = Image.fromarray((img_quantised*255).astype(np.uint8))
    if verbose:
        img_quantised.show()
    return img_quantised

# Grayllscale

img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = [[None, 0.5],[0.5, 0]], Grayscale = True, verbose = True)
img.save('Results/simple_kernel.jpg')

img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = 'Atkinson', Grayscale = True, verbose = True)
img.save('Results/atkinson_kernel.jpg')

img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = 'Floyd', Grayscale = True, verbose = True)
img.save('Results/floyd_kernel.jpg')

img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = 'Jarvis', Grayscale = True, verbose = True)
img.save('Results/jarvis_kernel.jpg')

# Full color

img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = [[None, 0.5],[0.5, 0]], Grayscale = False, verbose = True)
img.save('Results/simple_kernel.jpg')

img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = 'Atkinson', Grayscale = False, verbose = True)
img.save('Results/atkinson_kernel.jpg')

img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = 'Floyd', Grayscale = False, verbose = True)
img.save('Results/floyd_kernel.jpg')

img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = 'Jarvis', Grayscale = False, verbose = True)
img.save('Results/jarvis_kernel.jpg')
