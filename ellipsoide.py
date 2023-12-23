import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parametry elipsoidy
a = 1  # Półoś a
b = 2  # Półoś b
c = 3  # Półoś c

# Tworzenie siatki punktów na powierzchni elipsoidy
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 50)
phi, theta = np.meshgrid(phi, theta)

x = a * np.sin(theta) * np.cos(phi)
y = b * np.sin(theta) * np.sin(phi)
z = c * np.cos(theta)

# Tworzenie wykresu 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Narysowanie elipsoidy
ax.plot_surface(x, y, z, color='b', alpha=0.6, edgecolors='k')

# Ustawienia etykiet osi
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Ustawienia widoku
ax.view_init(elev=20, azim=30)

plt.show()
