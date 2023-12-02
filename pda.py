import time
import argparse
import matplotlib.pyplot as plt

import utils
import plot_on_surface
import isometic

parser = argparse.ArgumentParser(description="3D Scatter Plot with Title")
parser.add_argument("-t", "--title", type=str, default="", help="Title for the plot")
parser.add_argument("-f", "--file", type=str, default=None, help="File name od Point Cloud")
parser.add_argument(
    "-s", "--surface", type=str, default=None, nargs="+", help="Select surface of plotting"
)
parser.add_argument(
    "-r", "--range", type=str, default=1.0, help="Range of generating pointclouds [m]"
)
parser.add_argument(
    "-i", "--isometric", action="store_true", default=False, help="Isometric pointcloud plot"
)
args = parser.parse_args()

cloud = None
if args.file is None:
    lidar = utils.LidarConfig(16, 0.4, 2.0)
    cloud = utils.generate_pointcloud(lidar, float(args.range))

else:
    cloud = utils.read_pcd(args.file)


plt.ion()
if "XY" in args.surface:
    plot_on_surface.plot_on_xy("Punkty na płaszczyźnie XY", cloud)
if "YZ" in args.surface:
    plot_on_surface.plot_on_yz("Punkty na płaszczyźnie YZ", cloud)

if args.isometric:
    isometic.plot_3D("Chmura punktów w przestrzeni 3D", cloud)

while True:
    plt.pause(1000)
    time.sleep(1)
