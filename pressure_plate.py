# Set the transparency flag to True
transparency = True

# Set the transparency level to 2
transparency_level = 2

# Set the is_cube flag to False
is_cube = False

# Set the glass and translucent flags to False
glass = False
translucent = False

# Initialize an empty list to store colliders
colliders = []

# Define vertex positions for the top and bottom faces of the object
vertex_positions = [
    [0.5, -0.4375, 0.5, 0.5, -0.4375, -0.5, -0.5, -0.4375, -0.5, -0.5, -0.4375, 0.5],  # top face
    [-0.5, -0.4375, 0.5, -0.5, -0.4375, -0.5, 0.5, -0.4375, -0.5, 0.5, -0.4375, 0.5],  # bottom face
]

# Define texture coordinates for the top and bottom faces of the object
tex_coords = [
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # top face
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # bottom face
]

# Define shading values for the top and bottom faces of the object
shading_values = [
    [1.0, 1.0, 1.0, 1.0],  # top face
    [0.4, 0.4, 0.4, 0.4],  # bottom face
]

 
