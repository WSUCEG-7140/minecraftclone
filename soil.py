class MinecraftSoil:
    def __init__(self):
        # Define properties of the soil block in Minecraft

        # Whether the soil block is transparent (doesn't block light)
        self.transparent = True

        # Level of transparency (0 - fully opaque, 15 - fully transparent)
        self.transparency = 2

        # Whether the soil block is a full cube (True) or a slab (False)
        self.is_cube = False

        # Whether the soil block is made of glass (True) or not (False)
        self.glass = False

        # Whether the soil block is translucent (allows light to pass through partially)
        self.translucent = False

        # Define the collision box of the soil block
        self.colliders = [
            [
                (-0.5, -0.5000, -0.5),  # Minimum coordinates of the collider box
                (0.5, 0.4375, 0.5)      # Maximum coordinates of the collider box
            ]
        ]

        # Define the vertex positions of the soil block
        self.vertex_positions = [
            [0.5, 0.4375, 0.5,   0.5, -0.5, 0.5,   0.5, -0.5, -0.5,   0.5, 0.4375, -0.5],  # right
            [-0.5, 0.4375, -0.5,  -0.5, -0.5, -0.5,  -0.5, -0.5, 0.5,  -0.5, 0.4375, 0.5],  # left
            [0.5, 0.4375, 0.5,   0.5, 0.4375, -0.5,  -0.5, 0.4375, -0.5,  -0.5, 0.4375, 0.5],  # top
            [-0.5, -0.5, 0.5,  -0.5, -0.5, -0.5,   0.5, -0.5, -0.5,   0.5, -0.5, 0.5],        # bottom
            [-0.5, 0.4375, 0.5,  -0.5, -0.5, 0.5,   0.5, -0.5, 0.5,   0.5, 0.4375, 0.5],      # front
            [0.5, 0.4375, -0.5,   0.5, -0.5, -0.5,  -0.5, -0.5, -0.5,  -0.5, 0.4375, -0.5],  # back
        ]

        # Define the texture coordinates of the soil block
        self.tex_coords = [
            [0.0, 0.9375, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 0.9375, 0.0],
            [0.0, 0.9375, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 0.9375, 0.0],
            [0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
            [0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
            [0.0, 0.9375, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 0.9375, 0.0],
            [0.0, 0.9375, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 0.9375, 0.0],
        ]

        # Define the shading values of the soil block
        self.shading_values = [
            [0.6, 0.6, 0.6, 0.6],  # right
            [0.6, 0.6, 0.6, 0.6],  # left
            [1.0, 1.0, 1.0, 1.0],  # top
            [0.4, 0.4, 0.4, 0.4],  # bottom
            [0.8, 0.8, 0.8, 0.8],  # front
            [0.8, 0.8, 0.8, 0.8],  # back
        ]

