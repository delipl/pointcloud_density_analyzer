import matplotlib.pyplot as plt
import numpy as np
import math
import utils
import copy

def cart_to_sphere(x, y, z):
    r = math.sqrt(x*x + y*y + z*z)
    a = 0.0 
    b = 0.0
    if x != 0:
        a = math.atan(y/x)
    if r != 0:
        b = math.asin(z/r) # bo jest obrócony

    
    return np.array([
        r,
        a,
        b
    ])

def show_2D_XY_histogram(resolution=0.1, width=2.0, height=2.0):
    histogram_image_min = []
    histogram_image_max = []
    histogram_image_height = []

    image_width = int(height/ resolution)
    image_height = int(width / resolution)
    print(f"{image_width}, {image_height}")
    for i in range(image_width):
        column = [0] * image_height
        histogram_image_min.append(copy.copy(column))
        histogram_image_max.append(copy.copy(column))
        histogram_image_height.append(copy.copy(column))

    for i in range(image_width):
        for j in range(image_height):
            point_min = np.array([i * resolution, j*resolution - width/2.0, -1.34])
            model_height = 0.6
            point_max = np.array([i * resolution, j*resolution - width/2.0, -1.34 + model_height])
            intensity = 0
            
            offset = math.degrees(0.50)
            sphere_min_config = cart_to_sphere(point_min[0], point_min[1], point_min[2])
            sphere_max_config = cart_to_sphere(point_max[0], point_max[1], point_max[2])
            degrees_min = math.degrees(sphere_min_config[2])
            degrees_max= math.degrees(sphere_max_config[2])

            degrees_min +=offset
            degrees_max +=offset
            if (abs(degrees_min) < 15 ) and (abs(degrees_max) < 15 ):
                intensity = 1
            # print(f" min: {degrees_min}, max: {degrees_max}")
            if not (abs(degrees_min) < 15 ):
                degrees_min = 0
            else:
                degrees_min = 1
            if not (abs(degrees_max) < 15 ):
                degrees_max = 0
            else:
                degrees_max = 1


            histogram_image_min[image_width - i - 1][j] = degrees_min 
            histogram_image_max[image_width - i - 1][j] = degrees_max 
            histogram_image_height[image_width - i - 1][j] = intensity

    
    plt.figure()
    plt.title("Pozycje, w których czujnik widzi podstawę wspornika")
    plt.xlabel("Oś Y [m]", fontsize=8)
    plt.ylabel("Oś X [m]", fontsize=8)

    extent_values = [-2, 2, 0, 5]
    plt.imshow(histogram_image_min,  extent=extent_values)
    # plt.xticks(np.arange(-2, 3, 1))
    plt.grid()
    plt.colorbar()

    plt.figure()
    plt.title("Pozycje, w których czujnik widzi czubek wspornika")
    plt.xlabel("Oś Y [m]", fontsize=8)
    plt.ylabel("Oś X [m]", fontsize=8)
    plt.imshow(histogram_image_max, extent=extent_values)
    plt.grid()
    plt.colorbar()

    plt.figure()
    plt.title("Pozycje, w których czujnik widzi w całości wspornik")
    plt.xlabel("Oś Y [m]", fontsize=8)
    plt.ylabel("Oś X [m]", fontsize=8)
    plt.imshow(histogram_image_height, extent=extent_values)
    plt.grid()
    plt.colorbar()

    plt.show()
    



show_2D_XY_histogram(0.1, 4.0, 5.0)