class MinecraftButton:
    def __init__(self):
        # Define the property to determine if the button is transparent (can be seen through).
        self.bool_transparent = True

        # Define the level of transparency for the button.
        self.transparency = 2

        # Define whether the button is a cube or not (i.e., has three-dimensional depth).
        self.is_cube = False

        # Define if the button is made of glass material.
        self.glass = False

        # Define the property to determine if the button is translucent (partially see-through).
        self.bool_translucent = False

        # Define the list of colliders, which represents the collision bounds of the button.
        self.colliders = []

        # Define the vertex_positions list, which specifies the position of each vertex of the button.
        self.vertex_positions = [
            [0.5, 0.0, 0.5, 0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.0, -0.5],  # right
            [-0.5, 0.0, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.0, 0.5],  # left
            [0.5, 0.0, 0.5, 0.5, 0.0, -0.5, -0.5, 0.0, -0.5, -0.5, 0.0, 0.5],  # top
            [-0.5, -0.5, 0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5, 0.5],  # bottom
            [-0.5, 0.0, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.0, 0.5],  # front
            [0.5, 0.0, -0.5, 0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.0, -0.5],  # back
        ]

        # Define the texture coordinates list, which specifies how the texture is mapped to the button model.
        self.tex_coords = [
            [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.5, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
            [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.5, 0.0],
        ]

        # Define the shading values list, which represents the shading of each face of the button.
        self.shading_values = [
            [0.6, 0.6, 0.6, 0.6],   # Shading values for right face
            [0.6, 0.6, 0.6, 0.6],   # Shading values for left face
            [1.0, 1.0, 1.0, 1.0],   # Shading values for top face
            [0.4, 0.4, 0.4, 0.4],   # Shading values for bottom face
            [0.8, 0.8, 0.8, 0.8],   # Shading values for front face
            [0.8, 0.8, 0.8, 0.8],   # Shading values for back face
        ]

    def set_properties(self, transparent, transparency, is_cube, glass, translucent, colliders):
        # Set the button properties based on the given arguments.
        self.bool_transparent = transparent
        self.transparency = transparency
        self.is_cube = is_cube
        self.glass = glass
        self.bool_translucent = translucent
        self.colliders = colliders
