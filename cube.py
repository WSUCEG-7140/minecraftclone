class MinecraftCube:
    def __init__(self):
        # Cube properties
        self.transparent = False    # Determines if the cube is transparent
        self.transparency = 0       # Transparency value (0 to 1)
        self.is_cube = True         # Indicates if the object is a cube
        self.glass = False          # Specifies if the cube is made of glass material
        self.translucent = False    # Defines if the cube is translucent

        # Data structures to define the cube's shape
        self.colliders = [          # List of colliders (bounding boxes) for the cube
            [(-0.5, -0.5, -0.5), (0.5, 0.5, 0.5)]
        ]
        self.vertex_positions = [   # List of vertex positions for each face of the cube
            [0.5, 0.5, 0.5, 0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5],  # right
            [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5],  # left
            [0.5, 0.5, 0.5, 0.5, 0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5],  # top
            [-0.5, -0.5, 0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5, 0.5],  # bottom
            [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5],  # front
            [0.5, 0.5, -0.5, 0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5],  # back
        ]
        self.tex_coords = [         # Texture coordinates for each vertex of the cube
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # right
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # left
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # top
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # bottom
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # front
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # back
        ]

        self.shading_values = [    # Shading values for each face of the cube
            [0.6, 0.6, 0.6, 0.6],  # right
            [0.6, 0.6, 0.6, 0.6],  # left
            [1.0, 1.0, 1.0, 1.0],  # top
            [0.4, 0.4, 0.4, 0.4],  # bottom
            [0.8, 0.8, 0.8, 0.8],  # front
            [0.8, 0.8, 0.8, 0.8],  # back
        ]

    def set_properties(self, transparent, transparency, is_cube, glass, translucent, colliders):
        # Set properties of the cube
        self.transparent = transparent
        self.transparency = transparency
        self.is_cube = is_cube
        self.glass = glass
        self.translucent = translucent
        self.colliders = colliders
