import matplotlib.pyplot as plt
import numpy as np
import math
import argparse
from dataclasses import dataclass

from panda3d.core import Point3


@dataclass
class LidarConfig:
    num_of_layers: int
    vertical_angle_step: float
    horizontal_angle_step: float


def create_point_from_angles_and_range(v, h, r):
    point = Point3()
    point.x = r * math.cos(math.radians(h)) * math.cos(math.radians(v))
    point.y = r * math.cos(math.radians(h)) * math.sin(math.radians(v))
    point.z = r * math.sin(math.radians(h))
    return point


def generate_pointcloud(lidar: LidarConfig):
    start_horizontal_angle = -lidar.num_of_layers * lidar.horizontal_angle_step / 2
    start_vertical_angle = 45.0
    num_of_vertical_points = int(360 / lidar.vertical_angle_step)
    points = []
    for i in range(lidar.num_of_layers):
        for j in range(num_of_vertical_points):
            v = start_vertical_angle + j * lidar.vertical_angle_step
            h = start_horizontal_angle + i * lidar.horizontal_angle_step
            point = create_point_from_angles_and_range(v, h, 1.0)
            # self.create_and_display_edges([(0,0,0), point])
            points.append(point)
    return points


def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(theta / 2.0)
    b, c, d = -axis * math.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array(
        [
            [aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
            [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
            [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc],
        ]
    )


def read_pcd(file_path):
    points = []
    with open(file_path, "r") as f:
        for line in f:
            if line.startswith("DATA"):
                break
        for line in f:
            values = line.strip().split()
            if len(values) >= 3:
                x, y, z = float(values[0]), float(values[1]), float(values[2])
                point = np.array([x, y, z])
                points.append(point)

    return np.array(points)


# Sprawdzenie liczby argumentów wiersza poleceń
# Parsowanie argumentów wiersza poleceń
parser = argparse.ArgumentParser(description="3D Scatter Plot with Title")
parser.add_argument("-t", "--title", type=str, default="", help="Title for the plot")
parser.add_argument("-f", "--file", type=str, default="", help="File name od Point Cloud")
args = parser.parse_args()

# ax = plt.axes(projection='3d')
ax = plt.axes()
plt.grid()

cloud = []
# cloud = read_pcd(args.file)
# x = cloud[:, 0]
# y = cloud[:, 1]
# z = cloud[:, 2]
lidar = LidarConfig(16, 0.4, 2.0)
point_cloud = generate_pointcloud(lidar)
# print(point_cloud)
x = []
y = []
z = []
for point in point_cloud:
    x.append(point[0])
    y.append(point[1])
    z.append(point[2])


ax.set_xlabel("Oś X", fontsize=8)
ax.set_ylabel("Oś Y", fontsize=8)
# ax.set_zlabel('Oś Z', fontsize=8)
ax.tick_params(axis="both", labelsize=8)
plt.title(args.title)

# ax.scatter(x, y, z, s=[0.01 for i in range(len(x))],  marker='o', )
ax.plot(x, y)

# ax.set_box_aspect([np.ptp(coord) for coord in [x, y, z]])
# ax.view_init(azim=0, elev=0)

plt.tight_layout()

plt.show()
plt.savefig("test.svg", format="svg")
