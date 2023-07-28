# Set the transparency flag to True
transparent = True

# Set the transparency level to 2
transparency = 2

# Set the is_cube flag to False
is_cube = False

# Set the glass and translucent flags to False
glass = False
translucent = False

# Define a list of colliders. Each collider is a list of two points (tuples) defining a bounding box.
# The bounding box goes from the first point to the second point.
colliders = [
    [
        (-0.5, -0.5, -0.5),  # First point (bottom-left-back)
        (0.5, 0.0, 0.5)      # Second point (top-right-front)
    ]
]

# Define vertex positions for the object's faces
vertex_positions = [
    [0.5, 0.0, 0.5, 0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.0, -0.5],  # right face
    [-0.5, 0.0, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.0, 0.5],  # left face
    [0.5, 0.0, 0.5, 0.5, 0.0, -0.5, -0.5, 0.0, -0.5, -0.5, 0.0, 0.5],  # top face
    [-0.5, -0.5, 0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5, 0.5],  # bottom face
    [-0.5, 0.0, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.0, 0.5],  # front face
    [0.5, 0.0, -0.5, 0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.0, -0.5],  # back face
]

# Define texture coordinates for the object's faces
tex_coords = [
    [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.5, 0.0],  # right face
    [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.5, 0.0],  # left face
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # top face
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # bottom face
    [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.5, 0.0],  # front face
    [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.5, 0.0],  # back face
]

# Define shading values for the object's faces
shading_values = [
    [0.6, 0.6, 0.6, 0.6],  # right face
    [0.6, 0.6, 0.6, 0.6],  # left face
    [1.0, 1.0, 1.0, 1.0],  # top face
    [0.4, 0.4, 0.4, 0.4],  # bottom face
    [0.8, 0.8, 0.8, 0.8],  # front face
    [0.8, 0.8, 0.8, 0.8],  # back face
]
