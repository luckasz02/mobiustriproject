import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set up u and v parameters
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-1, 1, 50)
u, v = np.meshgrid(u, v)

# Parametric equations for the Mobius strip
x = (1 + v/2 * np.cos(u / 2)) * np.cos(u)
y = (1 + v/2 * np.cos(u / 2)) * np.sin(u)
z = v / 2 * np.sin(u / 2)

# Plotting the Mobius strip
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='cyan', edgecolor='k', alpha=0.7)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()