from PIL import Image
import numpy as np

def image_grayscale(path:str,verbose=True,n = 1):
    palete = np.array([0,1])
    img = np.array(Image.open(path))/255
    
    M = np.array([[0,2],[3,1]])
    M_pre = (M+1)/n - 0.5
    for row in range(img.shape(0)):
        for column in range(img.shape(1)):

            img(row,column,:) = 
    return img_contrasted



#factor = [3*0.2126,3*0.7152,3*0.0722]
#factor = [1,1,1]
factor = [3*0.299,3*0.587,3*0.114]
img_grayscale = image_grayscale(path = "Data/Lerik.jpg", verbose=True,factor = factor)
