import unittest
transparent = True
transparency = 2
is_cube = False
glass = False
translucent = False

colliders = []

#set values to vertext positions
vertex_positions = [
	[ 0.5, -0.4375,  0.5,   0.5, -0.4375, -0.5,  -0.5, -0.4375, -0.5,  -0.5, -0.4375,  0.5], # top
	[-0.5, -0.4375,  0.5,  -0.5, -0.4375, -0.5,   0.5, -0.4375, -0.5,   0.5, -0.4375,  0.5], # bottom
]

#set values to texture co-ordinates
tex_coords = [
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
]

#set shading values
shading_values = [
	[1.0, 1.0, 1.0, 1.0],
	[0.4, 0.4, 0.4, 0.4],
]
class minecraftFlatTestCases(unittest.TestCase):
    def test_flat_properties(self):
        # Test transparency property
        assert transparent is True

        # Test transparency value
        assert transparency == 2

        # Test is_cube property
        assert is_cube is False

        # Test glass property
        assert glass is False

        # Test translucent property
        assert translucent is False

    def test_flat_data_structures(self):
        # Test vertex_positions list
        assert len(vertex_positions) == 2
        assert len(vertex_positions[0]) == 12

        # Test tex_coords list
        assert len(tex_coords) == 2
        assert len(tex_coords[0]) == 12

        # Test shading_values list
        assert len(shading_values) == 2
        assert len(shading_values[0]) == 4


# Run the test cases
if __name__ == '__main__':
    unittest.main()
