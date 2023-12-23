import matplotlib.pyplot as plt
import numpy as np
import time
import numpy as np
import argparse
import matplotlib.pyplot as plt
import math
import utils
import sys

def plot_3D(title: str, cloud: np.array, cloud1: np.array):
    x = cloud[:, 0]
    y = cloud[:, 1]
    z = cloud[:, 2]
    i = np.array([])
    try:
        i = cloud[:, 3] 
    except IndexError:
        print("Oops!  That was no valid number.  Try again...")
   

    x1 = cloud1[:, 0]
    y1 = cloud1[:, 1]
    z1 = cloud1[:, 2]
    i1 = np.array([])
    try:
        i1 = cloud1[:, 3]
    except IndexError:
        print("Oops!  That was no valid number.  Try again...")


    plt.figure("Chmura punktów w przestrzeni 3D")
    ax = plt.axes(projection="3d")
    plt.grid()
    ax.set_xlabel("Oś X", fontsize=8)
    ax.set_ylabel("Oś Y", fontsize=8)
    ax.set_zlabel("Oś Z", fontsize=8)
    ax.tick_params(axis="both", labelsize=8)
    plt.title(title)
    color = "r"
    if len(i) > 0:
        color = i

    # Remove points in x1, y1, z1 that are already in x, y, z
    x1_unique, y1_unique, z1_unique, i1_unique = [], [], [], []
    for xi1, yi1, zi1 in zip(x1, y1, z1):
        found = False
        for xi, yi, zi in zip(x, y, z):

            d_x = xi1 - xi
            d_y = yi1 - yi
            d_z = zi1 - zi
            # print(d_x*d_x + d_y*d_y + d_z*d_z)
            if (d_x*d_x + d_y*d_y + d_z*d_z < 0.0001):
                found = True
                break
        if not found:
            x1_unique.append(xi1)
            y1_unique.append(yi1)
            z1_unique.append(zi1)
            

    ax.scatter3D(
        x,
        y,
        z,
        s=[0.8 for _ in range(len(x))],
        # c="b",
        c=color,
        marker="o",
        alpha=1,
        depthshade=False
    )
    ax.scatter3D(
        x1_unique,
        y1_unique,
        z1_unique,
        s=[0.01 for _ in range(len(x1_unique))],
        marker="o",
    )
    ax.set_box_aspect([np.ptp(coord) for coord in [x1, y1, z1]])
    ax.view_init(azim=-155, elev=20)

    plt.tight_layout()

    plt.show()

cloud = utils.read_pcd(sys.argv[2])
cloud1 = utils.read_pcd(sys.argv[3])
plot_3D(sys.argv[1], cloud, cloud1)
