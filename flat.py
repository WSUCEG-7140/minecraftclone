class MinecraftFlat:
    def __init__(self):
        """
        Initialize the MinecraftFlat class.

        This constructor initializes all the properties of the flat shape.
        """
        # Flat shape properties
        self.transparent = True     # Determines if the flat shape is transparent
        self.transparency = 2       # Transparency value (arbitrary value, might need to be changed)
        self.is_cube = False        # Indicates if the object is a cube (False for flat shape)
        self.glass = False          # Specifies if the flat shape is made of glass material
        self.translucent = False    # Defines if the flat shape is translucent

        # Data structures to define the flat shape's geometry
        self.colliders = []         # List of colliders (bounding boxes) for the flat shape (empty for flat shape)

        self.vertex_positions = [   # List of vertex positions for each face of the flat shape
            [0.5, -0.4375, 0.5, 0.5, -0.4375, -0.5, -0.5, -0.4375, -0.5, -0.5, -0.4375, 0.5],  # top face
            [-0.5, -0.4375, 0.5, -0.5, -0.4375, -0.5, 0.5, -0.4375, -0.5, 0.5, -0.4375, 0.5],  # bottom face
        ]

        self.tex_coords = [         # Texture coordinates for each vertex of the flat shape
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # top face texture coordinates
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # bottom face texture coordinates
        ]

        self.shading_values = [    # Shading values for each face of the flat shape
            [1.0, 1.0, 1.0, 1.0],  # top face shading values
            [0.4, 0.4, 0.4, 0.4],  # bottom face shading values
        ]

    def set_properties(self, transparent, transparency, is_cube, glass, translucent, colliders):
        """
        Set properties of the flat shape.

        Args:
            transparent (bool): Determines if the flat shape is transparent.
            transparency (int): Transparency value (arbitrary value, might need to be changed).
            is_cube (bool): Indicates if the object is a cube (False for flat shape).
            glass (bool): Specifies if the flat shape is made of glass material.
            translucent (bool): Defines if the flat shape is translucent.
            colliders (list): List of colliders (bounding boxes) for the flat shape (empty for flat shape).
        """
        # Set properties of the flat shape
        self.transparent = transparent
        self.transparency = transparency
        self.is_cube = is_cube
        self.glass = glass
        self.translucent = translucent
        self.colliders = colliders
