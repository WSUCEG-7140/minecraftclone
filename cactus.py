class MineCraftCactus:
    def __init__(self):
        # `properties` is a dictionary that stores various properties of the button.
        # The properties include:
        # - `transparent`: A boolean indicating if the button is transparent or not.
        # - `transparency`: An integer value representing the level of transparency of the button.
        # - `is_cube`: A boolean indicating if the button is cube-shaped or not.
        # - `glass`: A boolean indicating if the button is made of glass material.
        # - `translucent`: A boolean indicating if the button is translucent.
        self.properties = {
            'transparent': True,
            'transparency': 2,
            'is_cube': False,
            'glass': False,
            'translucent': False,
        }

        # `colliders` is a list of lists that represents the collision bounds of the button.
        # Each collider is represented as a pair of points, (lower_bound, upper_bound),
        # where each point is a tuple of (x, y, z) coordinates.
        self.colliders = []

        # `vertex_positions` is a list of lists that specifies the position of each vertex of the button.
        # Each list represents a face of the button, and each face has 12 vertices represented by (x, y, z) coordinates.
        self.vertex_positions = []

        # `tex_coords` is a list of lists that specifies how the texture is mapped to the button model.
        # Each list represents a face of the button, and each face has 12 texture coordinate pairs (u, v).
        self.tex_coords = []

        # `shading_values` is a list of lists that represents the shading of each face of the button.
        # Each list represents a face of the button, and each face has 4 shading values (r, g, b, a) for RGBA colors.
        self.shading_values = []

    def set_cactus_properties(self, transparent: bool, transparency: int, is_cube: bool, glass: bool, translucent: bool):
        # This method allows setting the properties of the button.
        # It takes arguments representing each property and updates the `properties` dictionary accordingly.
        self.properties['transparent'] = transparent
        self.properties['transparency'] = transparency
        self.properties['is_cube'] = is_cube
        self.properties['glass'] = glass
        self.properties['translucent'] = translucent

    def initialize_colliders(self):
        # This method initializes the `colliders` list with the collision bounds of the button.
        # It creates a single collider represented by a pair of points (lower_bound, upper_bound).
        # The button's collision bounds are specified as 3D coordinates (x, y, z).
        self.colliders = [
            [
                (-0.4375, -0.5, -0.4375),  # Lower bound of the collider
                (0.4375, 0.5, 0.4375)      # Upper bound of the collider
            ]
        ]

    def initialize_vertex_positions(self):
        # This method initializes the `vertex_positions` list with the position of each vertex of the button.
        # The button has 6 faces, and each face is represented by a list of 12 (x, y, z) coordinates.
        # Each coordinate represents the position of a vertex on that particular face.
        self.vertex_positions = [
            [0.4375, 0.5000, 0.5000, 0.4375, -0.5000, 0.5000, 0.4375, -0.5000, -0.5000, 0.4375, 0.5000, -0.5000],  # right
            [-0.4375, 0.5000, -0.5000, -0.4375, -0.5000, -0.5000, -0.4375, -0.5000, 0.5000, -0.4375, 0.5000, 0.5000],  # left
            [0.5000, 0.5000, 0.5000, 0.5000, 0.5000, -0.5000, -0.5000, 0.5000, -0.5000, -0.5000, 0.5000, 0.5000],  # top
            [-0.5000, -0.5000, 0.5000, -0.5000, -0.5000, -0.5000, 0.5000, -0.5000, -0.5000, 0.5000, -0.5000, 0.5000],  # bottom
            [-0.5000, 0.5000, 0.4375, -0.5000, -0.5000, 0.4375, 0.5000, -0.5000, 0.4375, 0.5000, 0.5000, 0.4375],  # front
            [0.5000, 0.5000, -0.4375, 0.5000, -0.5000, -0.4375, -0.5000, -0.5000, -0.4375, -0.5000, 0.5000, -0.4375],  # back
        ]

    def initialize_tex_coords(self):
        # This method initializes the `tex_coords` list with the texture coordinates for the button.
        # Each face of the button is represented by a list of 12 texture coordinate pairs (u, v).
        # These coordinates specify how the texture is mapped onto each face of the button.
        self.tex_coords = [
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
        ]

    def initialize_shading_values(self):
        # This method initializes the `shading_values` list with the shading values for each face of the button.
        # Each face is represented by a list of 4 shading values (r, g, b, a) for RGBA colors.
        # These values determine the shading of each face to achieve a 3D appearance.
        self.shading_values = [
            [0.6, 0.6, 0.6, 0.6],
            [0.6, 0.6, 0.6, 0.6],
            [1.0, 1.0, 1.0, 1.0],
            [0.4, 0.4, 0.4, 0.4],
            [0.8, 0.8, 0.8, 0.8],
            [0.8, 0.8, 0.8, 0.8],
        ]
