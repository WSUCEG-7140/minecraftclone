# Set transparency property to True
transparent = True

# Set transparency value to 2
transparency = 2

# Set is_cube property to False
is_cube = False

# Set glass property to False
glass = False

# Set translucent property to False
translucent = False

# Define the colliders list, which represents the collision bounds of the cactus
colliders = [
    [
        (-0.4375, -0.5, -0.4375),  # Lower bound of the collider
        (0.4375, 0.5, 0.4375)     # Upper bound of the collider
    ]
]

# Define the vertex positions list, which specifies the position of each vertex of the cactus
vertex_positions = [
    [0.4375, 0.5000, 0.5000, 0.4375, -0.5000, 0.5000, 0.4375, -
        0.5000, -0.5000, 0.4375, 0.5000, -0.5000],  # right
    [-0.4375, 0.5000, -0.5000, -0.4375, -0.5000, -0.5000, - \
        0.4375, -0.5000, 0.5000, -0.4375, 0.5000, 0.5000],  # left
    [0.5000, 0.5000, 0.5000, 0.5000, 0.5000, -0.5000, -0.5000,
        0.5000, -0.5000, -0.5000, 0.5000, 0.5000],  # top
    [-0.5000, -0.5000, 0.5000, -0.5000, -0.5000, -0.5000, 0.5000, - \
        0.5000, -0.5000, 0.5000, -0.5000, 0.5000],  # bottom
    [-0.5000, 0.5000, 0.4375, -0.5000, -0.5000, 0.4375,
        0.5000, -0.5000, 0.4375, 0.5000, 0.5000, 0.4375],  # front
    [0.5000, 0.5000, -0.4375, 0.5000, -0.5000, -0.4375, - \
        0.5000, -0.5000, -0.4375, -0.5000, 0.5000, -0.4375],  # back
]


