import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider

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
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])

def read_pcd(file_path):
    points = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('DATA'):
                break
        for line in f:
            values = line.strip().split()
            if len(values) >= 3:
                x, y, z = float(values[0]), float(values[1]), float(values[2])
                points.append(np.array([x, y, z]))
    return np.array(points)


# The parametrized function to be plotted
def f(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)

t = np.linspace(0, 1, 1000)

# Define initial parameters
init_amplitude = 5
init_frequency = 3

# Create the figure and the line that we will manipulate
cloud = read_pcd("to_histogram_pcds/histogram_ground_3129588.pcd")
x = cloud[:, 0]
y = cloud[:, 1]
z = cloud[:, 2]
fig, ax = plt.subplots()
pointlcoud_graph = ax.scatter(x, y, z)
ax.set_xlabel('x')

# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label='Frequency [Hz]',
    valmin=0.1,
    valmax=30,
    valinit=init_frequency,
)

# Make a vertically oriented slider to control the amplitude
axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
roll_slider = Slider(
    ax=axamp,
    label="roll",
    valmin=0,
    valmax=180,
    valinit=init_amplitude,
    orientation="vertical"
)

# The function to be called anytime a slider's value changes
def update(val):
    new_cloud = np.copy(cloud)
    for i in range(len(cloud)):
        new_cloud[i] = np.dot(rotation_matrix([0, 0, 1], roll_slider.val*math.pi/180.0), cloud[i])

    
    x_new = new_cloud[:, 0]
    y_new = new_cloud[:, 1]
    z_new = new_cloud[:, 2]
    ax.clear()
    pointlcoud_graph = ax.scatter(x_new, y_new, z_new)
    fig.canvas.draw_idle()


# register the update function with each slider
freq_slider.on_changed(update)
roll_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    freq_slider.reset()
    roll_slider.reset()
button.on_clicked(reset)

plt.show()