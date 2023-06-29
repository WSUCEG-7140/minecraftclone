transparent = True  # Indicates whether the cow model is transparent

transparency = 2  # The transparency level of the cow model

is_cube = False  # Indicates whether the cow model is a cube shape

glass = False  # Indicates whether the cow model has a glass material

translucent = False  # Indicates whether the cow model is translucent

# Defines the collision boundaries of the cow model
colliders = [
    [
        (-0.4375, -0.5, -0.4375),
        (0.4375, 0.5, 0.4375)
    ]
]


# Defines the texture coordinates of the cow model
tex_coords = [
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    # Texture coordinates for the top face
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    # Texture coordinates for the bottom face
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    # Texture coordinates for the front face
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    # Texture coordinates for the back face
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
] 

 # Defines the shading values of the cow model
shading_values = [
    [0.6, 0.6, 0.6, 0.6],  # Shading values for the right face
    [0.6, 0.6, 0.6, 0.6],  # Shading values for the left face
    [1.0, 1.0, 1.0, 1.0],  # Shading values for the top face
    [0.4, 0.4, 0.4, 0.4],  # Shading values for the bottom face
    [0.8, 0.8, 0.8, 0.8],  # Shading values for the front face
    [0.8, 0.8, 0.8, 0.8],  # Shading values for the back face
] 
