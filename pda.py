import time
import numpy as np
import argparse
import matplotlib.pyplot as plt
import math
import utils
import plot_on_surface
import isometic
import histogram

parser = argparse.ArgumentParser(description="3D Scatter Plot with Title")
parser.add_argument("-t", "--title", type=str, default="", help="Title for the plot")
parser.add_argument("-f", "--file", type=str, default=None, help="File name od Point Cloud")
parser.add_argument(
    "-s", "--surface", type=str, default=[], nargs="+", help="Select surface of plotting"
)
parser.add_argument(
    "-r", "--range", type=str, default=1.0, help="Range of generating pointclouds [m]"
)
parser.add_argument(
    "-i", "--isometric", action="store_true", default=False, help="Isometric pointcloud plot"
)
parser.add_argument(
    "-his", "--histogram", type=str, default=[], nargs="+", help="Histogram of Pointcloud"
)

args = parser.parse_args()

cloud = None
if args.file is None:
    lidar = utils.LidarConfig(16, 0.4, 2.0)
    cloud = utils.generate_pointcloud(lidar, float(args.range))
    x = cloud[:, 0]
    y = cloud[:, 1]
    z = cloud[:, 2]
    x += float(args.range)
    z += float(args.range)/4.0 * math.sin(lidar.horizontal_angle_step)

else:
    cloud = utils.read_pcd(args.file)
    cloud = np.array([point for point in cloud if (point[0]*point[0] + point[1]*point[1] + point[2]*point[2])<200])
    print(cloud)

x = cloud[:, 0]
y = cloud[:, 1]
z = cloud[:, 2]

x_min = min(x)
y_min = min(y)
z_min = min(z)
x_max = max(x)
y_max = max(y)
z_max = max(z)
print(y_min)
print(y_max)

plt.ion()
if "XY" in args.surface:
    plot_on_surface.plot_on_xy("Punkty na płaszczyźnie XY", cloud)
if "YZ" in args.surface:
    plot_on_surface.plot_on_yz("Punkty na płaszczyźnie YZ", cloud)

if args.isometric:
    isometic.plot_3D("Chmura punktów w przestrzeni 3D", cloud)

if "XY" in args.histogram:
    histogram.show_2D_XY_histogram(cloud, 0.1, x_max - x_min, y_max - y_min)
if "YZ" in args.histogram:
    histogram.show_2D_YZ_histogram(cloud, 0.1, y_max - y_min, z_max - z_min)
while True:
    plt.pause(1000)
    time.sleep(1)
