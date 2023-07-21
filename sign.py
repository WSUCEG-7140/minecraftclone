# Set transparency-related properties
transparent = True           # Indicates if the object is transparent
transparency = 2             # Transparency level (adjust as needed)
is_cube = False              # Indicates if the object is a cube (can be used for collision detection)
glass = False                # Indicates if the object is made of glass (a specific type of transparency)
translucent = False          # Indicates if the object is translucent (allows some light to pass through)

# Initialize colliders list (can be used to store colliders for the object)
colliders = []

# Define vertex positions for the object
vertex_positions = [
	[-0.3536, 0.5000,  0.3536, -0.3536, -0.5000,  0.3536,  0.3536, -0.5000, -0.3536,  0.3536, 0.5000, -0.3536],  # Face 1
	[-0.3536, 0.5000, -0.3536, -0.3536, -0.5000, -0.3536,  0.3536, -0.5000,  0.3536,  0.3536, 0.5000,  0.3536],  # Face 2
	[ 0.3536, 0.5000, -0.3536,  0.3536, -0.5000, -0.3536, -0.3536, -0.5000,  0.3536, -0.3536, 0.5000,  0.3536],  # Face 3
	[ 0.3536, 0.5000,  0.3536,  0.3536, -0.5000,  0.3536, -0.3536, -0.5000, -0.3536, -0.3536, 0.5000, -0.3536],  # Face 4
]

# Define texture coordinates for the object
tex_coords = [
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # Face 1
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # Face 2
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # Face 3
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],  # Face 4
]

# Define shading values for the object
shading_values = [
	[1.0, 1.0, 1.0, 1.0],  # Face 1
	[1.0, 1.0, 1.0, 1.0],  # Face 2
	[1.0, 1.0, 1.0, 1.0],  # Face 3
	[1.0, 1.0, 1.0, 1.0],  # Face 4
]
