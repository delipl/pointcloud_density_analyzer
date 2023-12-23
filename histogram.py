import matplotlib.pyplot as plt
import numpy as np

def show_2D_YZ_histogram(cloud, resolution=0.1, width=2.0, height=2.0):
    histogram_image = []

    image_width = int(width / resolution)
    image_height = int(height / resolution)

    for _ in range(image_height):
        column = [0] * image_width
        histogram_image.append(column)

    for point in cloud:
        image_width_pos = int((width / 2 + point[1]) / resolution)
        image_height_pos = int(image_height) - int(point[2] / resolution) - 1
        if image_height_pos < 0 or image_width_pos < 0:
            continue
        if image_width_pos >= image_width or image_height_pos >= image_height:
            continue
        histogram_image[image_height_pos][image_width_pos] += 1

    plt.figure("Histogram 2D YZ")
    plt.title("Histogram 2D YZ")
    plt.xlabel("Oś Y [m]", fontsize=8)
    plt.ylabel("Oś Z [m]", fontsize=8)
    extent_values = [-2, 2, 0, 1.5]
    img = plt.imshow(histogram_image, extent=extent_values)
    img.set_clim(0, 270)
    plt.colorbar()

    plt.figure("Histogram YZ")
    plt.title("Histogram YZ")
    plt.xlabel("Ilość punktów w sektorze", fontsize=12)
    plt.ylabel("Ilość sektorów", fontsize=12)
    plt.grid()
    densities = []
    for column in histogram_image:
        column = [x for x in column if x != 0]
        densities += column
    densities = np.array(densities)

    plt.hist(densities, bins=np.arange(min(densities), max(densities) + 1, 1),
             align='left')
 
    plt.xticks(np.arange(min(densities), max(densities) + 1, 11))

    return histogram_image

def show_2D_XY_histogram(cloud, resolution=0.1, width=2.0, height=2.0):
    histogram_image = []

    image_width = int(height/ resolution)
    image_height = int(width / resolution)

    for _ in range(image_height):
        column = [0] * image_width
        histogram_image.append(column)

    for point in cloud:
        image_width_pos = int(image_width / 2) - int (point[1] / resolution)
        image_height_pos = int(image_height) - int(point[0] / resolution) - 1
        if image_height_pos < 0 or image_width_pos < 0:
            continue
        if image_width_pos >= image_width or image_height_pos >= image_height:
            continue
        histogram_image[image_height_pos][image_width_pos] += 1

    plt.figure("Histogram 2D YX")
    plt.title("Histogram 2D YX")
    plt.xlabel("Oś Y [m]", fontsize=8)
    plt.ylabel("Oś X [m]", fontsize=8)
    extent_values = [-2, 2, 0, 5]
    img = plt.imshow(histogram_image, extent=extent_values)
    img.set_clim(0, 80)
    plt.colorbar()

    plt.figure("Histogram YX")
    plt.title("Histogram YX")
    plt.xlabel("Ilość punktów w sektorze", fontsize=12)
    plt.ylabel("Ilość sektorów", fontsize=12)
    plt.grid()

    densities = []
    for column in histogram_image:
        column = [x for x in column if x != 0]
        densities += column
    densities = np.array(densities)

    plt.hist(densities, bins=np.arange(min(densities), max(densities) + 1, 1),
             align='left')
    plt.xticks(np.arange(min(densities), max(densities) + 1, 11))

    return histogram_image
