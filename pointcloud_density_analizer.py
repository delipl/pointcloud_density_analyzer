import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
from matplotlib.ticker import AutoMinorLocator, MultipleLocator


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
                point = np.dot(rotation_matrix([0, 0, 1], math.pi / 2.0), point)
                points.append(point)

    return np.array(points)


def to_top_view(cloud):
    top_cloud = np.copy(cloud)
    for i in range(len(cloud)):
        top_cloud[i] += np.array([0.0, 0.1, 0.0])

        top_cloud[i] = np.dot(rotation_matrix([1, 0, 0], math.pi / 2.0), top_cloud[i])
        top_cloud[i] = np.dot(rotation_matrix([0, 0, 1], math.pi), top_cloud[i])
    return top_cloud

def rotate_cloud(cloud, roll, pitch, yaw):
    new_cloud = np.copy(cloud)
    for i in range(len(cloud)):
        new_cloud[i] = np.dot(
            rotation_matrix([0, 0, 1], roll * math.pi / 180.0), cloud[i]
        )
        new_cloud[i] = np.dot(
            rotation_matrix([0, 1, 0], pitch * math.pi / 180.0), new_cloud[i]
        )
        new_cloud[i] = np.dot(
            rotation_matrix([1, 0, 0], yaw * math.pi / 180.0), new_cloud[i]
        )
    return new_cloud
    
def generate_density_image(cloud, resolution: float, width: float, height: float):
    histogram_image = []

    image_width = int(width / resolution)
    image_height = int(height / resolution)

    for _ in range(image_height):
        column = [0] * image_width
        histogram_image.append(column)

    for point in cloud:
        image_width_pos = int((width / 2 + point[0]) / resolution)
        image_height_pos = int(point[1] / resolution)

        if image_width_pos >= image_width or image_height - image_height_pos -1 >= image_height:
            continue
        histogram_image[image_height - image_height_pos -1][image_width_pos] += 1

    return histogram_image




def update_plot(axis, cloud):
    x = cloud[:, 0]
    y = cloud[:, 1]
    z = cloud[:, 2]
    axis.clear()
    axis.set_xlabel("y")
    axis.set_ylabel("z")
    axis.grid()
    axis.scatter(x, y, z, c=[1 for i in range(len(x))])

def update_histogram(axis, data):
    axis.clear()
    axis.set_xlabel("density")
    axis.set_ylabel("count")
    axis.grid()
    axis.hist(data)

# Window and plots:
fig, ((ax, az), (ix, iz), (hx, hz)) = plt.subplots(3, 2)
# Sliders
axamp = fig.add_axes([0.05, 0.6, 0.0225, 0.2])
roll_slider = Slider(
    ax=axamp, label="roll", valmin=-45, valmax=45, valinit=1.8, orientation="vertical"
)

axamp = fig.add_axes([0.10, 0.6, 0.0225, 0.2])
pitch_slider = Slider(
    ax=axamp,
    label="pitch",
    valmin=-45,
    valmax=45,
    valinit=-1.2,
    orientation="vertical",
)

axamp = fig.add_axes([0.15, 0.6, 0.0225, 0.2])
yaw_slider = Slider(
    ax=axamp, label="yaw", valmin=-45, valmax=45, valinit=0, orientation="vertical"
)

axamp = fig.add_axes([0.075, 0.3, 0.0225, 0.2])
front_resolution_slider = Slider(
    ax=axamp, label="Front res", valmin=0.01, valmax=0.2, valinit=0.1, orientation="vertical"
)

axamp = fig.add_axes([0.125, 0.3, 0.0225, 0.2])
top_resolution_slider = Slider(
    ax=axamp, label="Top res", valmin=0.01, valmax=0.2, valinit=0.1, orientation="vertical"
)

# Create the figure and the line that we will manipulate
cloud = read_pcd("to_histogram_pcds/histogram_ground_3129588.pcd")
front_rotated_cloud = []
top_rotated_cloud = []


rotated = rotate_cloud(cloud, 180, 0,0)

rotated = rotate_cloud(rotated, roll_slider.val, pitch_slider.val, yaw_slider.val)
update_plot(ax, rotated)
front_rotated_cloud = np.copy(rotated)

fig.subplots_adjust(left=0.25)
top_cloud = to_top_view(cloud)
update_plot(az, top_cloud)
top_rotated_cloud = np.copy(top_cloud)


front_density_image = generate_density_image(rotated, front_resolution_slider.val, 2.4, 1.0)
ix.imshow(front_density_image)
top_density_image = generate_density_image(top_cloud, top_resolution_slider.val, 2.4, 4.0)
iz.imshow(top_density_image)

update_histogram(hx, front_density_image)
update_histogram(hz, top_density_image)



# The function to be called anytime a slider's value changes


def update(val):
    global front_rotated_cloud
    global top_rotated_cloud

    # ix.imshow()
    front_rotated_cloud = rotate_cloud(rotated, roll_slider.val, pitch_slider.val, yaw_slider.val)
    top_rotated_cloud = to_top_view(front_rotated_cloud)
    update_plot(ax, front_rotated_cloud)
    update_plot(az, top_rotated_cloud)

    front_density_image = generate_density_image(front_rotated_cloud, front_resolution_slider.val, 2.4, 1.0)
    ix.imshow(front_density_image)
    top_density_image = generate_density_image(top_rotated_cloud, top_resolution_slider.val, 2.4, 4.0)
    iz.imshow(top_density_image)
    hx.hist(front_density_image)

    update_histogram(hx, front_density_image)
    update_histogram(hz, top_density_image)
    fig.canvas.draw_idle()
    




# # register the update function with each slider
roll_slider.on_changed(update)
pitch_slider.on_changed(update)
yaw_slider.on_changed(update)

def update_front_image(val):
    global front_rotated_cloud
    front_density_image = generate_density_image(front_rotated_cloud, front_resolution_slider.val, 2.4, 1.0)
    ix.imshow(front_density_image)
    update_histogram(hx, front_density_image)



def update_top_image(val):
    global top_rotated_cloud
    top_density_image = generate_density_image(top_rotated_cloud, top_resolution_slider.val, 2.4, 4.0)
    iz.imshow(top_density_image)
    update_histogram(hz, top_density_image)


front_resolution_slider.on_changed(update_front_image)
top_resolution_slider.on_changed(update_top_image)


def reset(event):
    freq_slider.reset()
    roll_slider.reset()
    pitch_slider.reset()
    yaw_slider.reset()


plt.show()
