class MinecraftButton:
    def __init__(self):
        self.transparent = True
        self.transparency = 2
        self.is_cube = False
        self.glass = False
        self.translucent = False
        self.colliders = []
        self.vertex_positions = [
            [0.5, 0.0, 0.5, 0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.0, -0.5],  # right
            [-0.5, 0.0, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.0, 0.5],  # left
            [0.5, 0.0, 0.5, 0.5, 0.0, -0.5, -0.5, 0.0, -0.5, -0.5, 0.0, 0.5],  # top
            [-0.5, -0.5, 0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5, 0.5],  # bottom
            [-0.5, 0.0, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.0, 0.5],  # front
            [0.5, 0.0, -0.5, 0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.0, -0.5],  # back
        ]
        self.tex_coords = [
            [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.5, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
            [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.5, 0.0],
        ]
        self.shading_values = [
            [0.6, 0.6, 0.6, 0.6],
            [0.6, 0.6, 0.6, 0.6],
            [1.0, 1.0, 1.0, 1.0],
            [0.4, 0.4, 0.4, 0.4],
            [0.8, 0.8, 0.8, 0.8],
            [0.8, 0.8, 0.8, 0.8],
        ]
    def set_properties(self, transparent, transparency, is_cube, glass, translucent, colliders):
        self.transparent = transparent
        self.transparency = transparency
        self.is_cube = is_cube
        self.glass = glass
        self.translucent = translucent
        self.colliders = colliders
