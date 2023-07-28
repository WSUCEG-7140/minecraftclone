class MinecraftLiquid:
    def __init__(self):
        """
        Initialize the MinecraftLiquid class.

        This constructor initializes all the properties of the liquid block.
        """
        # Liquid block properties
        self.transparent = True     # Determines if the liquid block is transparent
        self.transparency = 1       # Transparency value (arbitrary value, might need to be changed)
        self.is_cube = True         # Indicates if the object is a cube (True for liquid block)
        self.glass = True           # Specifies if the block has a glass-like appearance
        self.translucent = True     # Defines if the liquid block is translucent

        # Define the colliders (bounding boxes) for the liquid block
        self.colliders = []

        # Define the vertex positions for each face of the liquid block
        self.vertex_positions = [
            [0.500,  0.375,  0.500,   0.500, -0.625,  0.500,   0.500, -0.625, -0.500,   0.500,  0.375, -0.500],   # right face
            [-0.500,  0.375, -0.500,  -0.500, -0.625, -0.500,  -0.500, -0.625,  0.500,  -0.500,  0.375,  0.500],   # left face
            [0.500,  0.375,  0.500,   0.500,  0.375, -0.500,  -0.500,  0.375, -0.500,  -0.500,  0.375,  0.500],   # top face
            [-0.500, -0.625,  0.500,  -0.500, -0.625, -0.500,   0.500, -0.625, -0.500,   0.500, -0.625,  0.500],   # bottom face
            [-0.500,  0.375,  0.500,  -0.500, -0.625,  0.500,   0.500, -0.625,  0.500,   0.500,  0.375,  0.500],   # front face
            [0.500,  0.375, -0.500,   0.500, -0.625, -0.500,  -0.500, -0.625, -0.500,  -0.500,  0.375, -0.500],   # back face
        ]

        # Define the texture coordinates for each vertex of the liquid block
        self.tex_coords = [
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],   # right face texture coordinates
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],   # left face texture coordinates
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],   # top face texture coordinates
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],   # bottom face texture coordinates
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],   # front face texture coordinates
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],   # back face texture coordinates
        ]
		# set shading values
        self.shading_values = [
		[0.6, 0.6, 0.6, 0.6],
		[0.6, 0.6, 0.6, 0.6],
		[1.0, 1.0, 1.0, 1.0],
		[0.4, 0.4, 0.4, 0.4],
		[0.8, 0.8, 0.8, 0.8],
		[0.8, 0.8, 0.8, 0.8],
	]



