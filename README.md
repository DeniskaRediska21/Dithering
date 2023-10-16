# Dithering

A numer of Dithering methods implemented in python

Methods:
+ Bayer Dithering
+ White Noise Dithering
+ Blue Noise Dithering
+ Custom Kernel Dithering (which includes methods: Atkinson, Floyd-Steinberg, Jarvis-Judice-Ninke dithering)

## Bayer Dithering

```
img = bayer_dither('Data/Penguins.jpg',num_colors = 2,kernel_size = 2,scale_factor = 0.1,Binary_dithering = False,Grayscale = False,verbose = True)
img = bayer_dither('Data/Penguins.jpg',num_colors = 2,kernel_size = 2,scale_factor = 0.1,Binary_dithering = True,Grayscale = True,verbose = True)
```

| Original                       | Bayer Grayscale                              | Bayer Full-Color                                           |
|--------------------------------|----------------------------------------------|------------------------------------------------------------|
| ![Original](Data/Penguins.jpg) | ![Bayer Grayscale](Results/bayer_binary.jpg) | ![Bayer Full-Color](Results/bayer_full_color_additive.jpg) |

## White Noise Dithering

```
img = white_noise_dither('Data/Penguins.jpg', num_colors = 2, scale_factor = 0.1, Binary_dithering = True, Grayscale = True)
img = white_noise_dither('Data/Penguins.jpg', num_colors = 2, scale_factor = 0.1, Binary_dithering = True, Grayscale = False)
```

| Original                       | White Noise Grayscale                                              | White Noise Full-Color                                               |
|--------------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------|
| ![Original](Data/Penguins.jpg) | ![White Noise Grayscale](Results/white_noise_dither_grayscale.jpg) | ![White Noise Full-Color](Results/white_noise_dither_full_color.jpg) |

## Blue Noise Ditheringi

```
img = blue_noise_dither('Data/Penguins.jpg',num_colors = 2, scale_factor = 1, sigma = 5, Binary_dithering = True, Grayscale = True)
img = blue_noise_dither('Data/Penguins.jpg',num_colors = 2, scale_factor = 1, sigma = 5, Binary_dithering = True, Grayscale = False)
```

| Original                       | Blue Noise Grayscale                                             | Blue Noise Full-Color                                              |
|--------------------------------|------------------------------------------------------------------|--------------------------------------------------------------------|
| ![Original](Data/Penguins.jpg) | ![Blue Noise Grayscale](Results/blue_noise_dither_grayscale.jpg) | ![Blue Noise Full-Color](Results/blue_noise_dither_full_color.jpg) |

## Custom Kernel Dithering

```
img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = [[None, 0.5],[0.5, 0]], Grayscale = True, verbose = True)
img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = [[None, 0.5],[0.5, 0]], Grayscale = False, verbose = True)
```

| Original                       | Simple Error Diffusion Grayscale                                         | Simple Error Diffusion Full-Color                                    |
|--------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------|
| ![Original](Data/Penguins.jpg) | ![Simple Error Diffusion Grayscale](Results/simple_kernel_grayscale.jpg) | ![Simple Error Diffusion Full-Color](Results/simple_kernel_full.jpg) |

```
img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = 'Atkinson', Grayscale = True, verbose = True)
img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = 'Atkinson', Grayscale = False, verbose = True)
```

| Original                       | Atkinson Grayscale                                          | Atkinson Full-Color                                     |
|--------------------------------|-------------------------------------------------------------|---------------------------------------------------------|
| ![Original](Data/Penguins.jpg) | ![Atkinson Grayscale](Results/atinson_kernel_grayscale.jpg) | ![Atkinson Full-Color](Results/atinson_kernel_full.jpg) |

```
img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = 'Floyd', Grayscale = True, verbose = True)
img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = 'Floyd', Grayscale = False, verbose = True)
```
| Original                       | Floyd-Steinberg Grayscale                                        | Floyd-Steinberg Full-Color                                        |
|--------------------------------|------------------------------------------------------------------|-------------------------------------------------------------------|
| ![Original](Data/Penguins.jpg) | ![Floyd-Steinberg Grayscale](Results/floyd_kernel_grayscale.jpg) | ![Floyd-Steinberg Full-Color](Results/floyd_kernel_grayscale.jpg) |

```
img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = 'Jarvis', Grayscale = True, verbose = True)
img = custom_kernel_dither('Data/Penguins.jpg',num_colors = 2, Kernel = 'Jarvis', Grayscale = False, verbose = True)
```
| Original                       | Jarvis-Judice-Ninke Grayscale                                         | Jarvis-Judice-Ninke Full-Color                                    |
|--------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------|
| ![Original](Data/Penguins.jpg) | ![Jarvis-Judice-Ninke Grayscale](Results/jarvis_kernel_grayscale.jpg) | ![Jarvis-Judice-Ninke Full-Color](Results/jarvis_kernel_full.jpg) |
