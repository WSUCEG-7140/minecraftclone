class MinecraftGlass:
    def __init__(self):
        """
        Initialize the MinecraftGlass class.

        This constructor initializes all the properties of the glass block.
        """
        # Glass block properties
        self.transparent = True     # Determines if the glass block is transparent
        self.transparency = 2       # Transparency value (arbitrary value, might need to be changed)
        self.is_cube = True         # Indicates if the object is a cube (True for glass block)
        self.glass = True           # Specifies if the block is made of glass material
        self.translucent = False    # Defines if the glass block is translucent

        # Define the colliders (bounding boxes) for the glass block
        self.colliders = [
            [
                (-0.5, -0.5, -0.5),   # Collider minimum point for x, y, z
                (0.5,  0.5,  0.5)     # Collider maximum point for x, y, z
            ]
        ]

        # Define the vertex positions for each face of the glass block
        self.vertex_positions = [
            [0.5,  0.5,  0.5,  0.5, -0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5],   # right face
            [-0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5,  0.5,  0.5],  # left face
            [0.5,  0.5,  0.5,  0.5,  0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5,  0.5],   # top face
            [-0.5, -0.5,  0.5, -0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5, -0.5,  0.5],  # bottom face
            [-0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5,  0.5,  0.5,  0.5,  0.5],  # front face
            [0.5,  0.5, -0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5],   # back face
        ]

        # Define the texture coordinates for each vertex of the glass block
        self.tex_coords = [
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],   # right face texture coordinates
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],   # left face texture coordinates
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],   # top face texture coordinates
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],   # bottom face texture coordinates
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],   # front face texture coordinates
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],   # back face texture coordinates
        ]

        # Define shading values for each face of the glass block
        self.shading_values = [
            [0.6, 0.6, 0.6, 0.6],   # right face shading values
            [0.6, 0.6, 0.6, 0.6],   # left face shading values
            [1.0, 1.0, 1.0, 1.0],   # top face shading values
            [0.4, 0.4, 0.4, 0.4],   # bottom face shading values
            [0.8, 0.8, 0.8, 0.8],   # front face shading values
            [0.8, 0.8, 0.8, 0.8],   # back face shading values
        ]
