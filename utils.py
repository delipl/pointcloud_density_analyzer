import numpy as np
import math
from dataclasses import dataclass


@dataclass
class LidarConfig:
    num_of_layers: int
    vertical_angle_step: float
    horizontal_angle_step: float


def create_point_from_angles_and_range(v: float, h: float, r: float):
    """
    Return one point of vertical, horizontal angle and r range
    """
    point = [0, 0, 0]
    point[0] = r * math.cos(math.radians(h)) * math.cos(math.radians(v))
    point[1] = r * math.cos(math.radians(h)) * math.sin(math.radians(v))
    point[2] = r * math.sin(math.radians(h))
    return np.array(point)


def generate_pointcloud(lidar: LidarConfig, r=1.0):
    """
    From the LidarConfig generate full pointcloud in default r=1m range and
    return np.array od points
    """
    start_horizontal_angle = -lidar.num_of_layers * lidar.horizontal_angle_step / 2
    start_vertical_angle = 45.0
    num_of_vertical_points = int(360 / lidar.vertical_angle_step)
    points = []
    for i in range(lidar.num_of_layers):
        for j in range(num_of_vertical_points):
            v = start_vertical_angle + j * lidar.vertical_angle_step
            h = start_horizontal_angle + i * lidar.horizontal_angle_step
            points.append(create_point_from_angles_and_range(v, h, r))

    return np.array(points)


def rotation_matrix(axis: list, theta: float):
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
    """
    Read pointcloud from pcd file and return np.array of 3d points
    """
    points = []
    with open(file_path, "r", encoding="utf8") as f:
        for line in f:
            if line.startswith("DATA"):
                break
        for line in f:
            values = line.strip().split()
            if len(values) == 3:
                x, y, z = float(values[0]), float(values[1]), float(values[2])
                point = np.array([x, y, z])
                points.append(point)
            elif len(values) == 4:
                x, y, z, i = float(values[0]), float(values[1]), float(values[2]), float(values[3])
                point = np.array([x, y, z, i])
                points.append(point)


    return np.array(points)
