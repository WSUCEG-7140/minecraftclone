class Minecraft:
    def __init__(self):
        self.transparent = True
        self.is_cube = False
        self.glass = False
        self.colliders = []
        self.bones = [
            {
                'name': 'body',
                'pivot': [0.0, 0.8125, 0.125],
                'vertices': [[...]],  # Truncated for brevity
                'tex_coords': [[...]],  # Truncated for brevity
                'shading_values': [[...]]  # Truncated for brevity
            },
            {
                'name': 'head',
                'pivot': [0.0, 0.75, -0.375],
                'vertices': [[...]],  # Truncated for brevity
                'tex_coords': [[...]],  # Truncated for brevity
                'shading_values': [[...]]  # Truncated for brevity
            },
            # Add more bones here if needed
        ]

    def add_bone(self, bone_data):
        self.bones.append(bone_data)

    def remove_bone(self, bone_name):
        self.bones = [bone for bone in self.bones if bone['name'] != bone_name]

    def set_glass(self, value):
        self.glass = value

    def add_collider(self, collider_data):
        self.colliders.append(collider_data)

    # Add more methods here for other functionalities if needed



