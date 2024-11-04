def euler_characteristic(vertices, edges, faces):
    return vertices - edges + faces

# Example of a triangulated surface
vertices = 6
edges = 9
faces = 3

chi = euler_characteristic(vertices, edges, faces)
print(f"Euler Characteristic: {chi}")