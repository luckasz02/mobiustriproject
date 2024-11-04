import numpy as np
import plotly.graph_objects as go

# Set up u and v parameters
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-1, 1, 50)
u, v = np.meshgrid(u, v)

# Parametric equations for the Möbius strip
x = (1 + v/2 * np.cos(u / 2)) * np.cos(u)
y = (1 + v/2 * np.cos(u / 2)) * np.sin(u)
z = v / 2 * np.sin(u / 2)

# Create a 3D surface plot
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Viridis')])

# Customize layout
fig.update_layout(
    title='Interactive Möbius Strip',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    )
)

# Show the interactive plot
fig.show()