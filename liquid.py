import unittest
# in the end, it'd be nice to have it so that liquids fill up the whole block when they have a block above them
# this would avoid the problems this solution has
transparent = True
transparency = 1
is_cube = True
glass = True
translucent = True

colliders = []

#set vertext positions 
vertex_positions = [
	[ 0.500,  0.375,  0.500,   0.500, -0.625,  0.500,   0.500, -0.625, -0.500,   0.500,  0.375, -0.500], # right
	[-0.500,  0.375, -0.500,  -0.500, -0.625, -0.500,  -0.500, -0.625,  0.500,  -0.500,  0.375,  0.500], # left
	[ 0.500,  0.375,  0.500,   0.500,  0.375, -0.500,  -0.500,  0.375, -0.500,  -0.500,  0.375,  0.500], # top
	[-0.500, -0.625,  0.500,  -0.500, -0.625, -0.500,   0.500, -0.625, -0.500,   0.500, -0.625,  0.500], # bottom
	[-0.500,  0.375,  0.500,  -0.500, -0.625,  0.500,   0.500, -0.625,  0.500,   0.500,  0.375,  0.500], # front
	[ 0.500,  0.375, -0.500,   0.500, -0.625, -0.500,  -0.500, -0.625, -0.500,  -0.500,  0.375, -0.500], # back
]

#set texture co-ordinates
tex_coords = [
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
]

#set shading values
shading_values = [
	[0.6, 0.6, 0.6, 0.6],
	[0.6, 0.6, 0.6, 0.6],
	[1.0, 1.0, 1.0, 1.0],
	[0.4, 0.4, 0.4, 0.4],
	[0.8, 0.8, 0.8, 0.8],
	[0.8, 0.8, 0.8, 0.8],
]
class minecraftLiquidTestCases(unittest.TestCase):
    def test_liquid_properties(self):
        # Test transparency property
        assert transparent is True

        # Test transparency value
        assert transparency == 1

        # Test is_cube property
        assert is_cube is True

        # Test glass property
        assert glass is True

        # Test translucent property
        assert translucent is True

    def test_liquid_data_structures(self):
        # Test vertex_positions list
        assert len(vertex_positions) == 6
        assert len(vertex_positions[0]) == 12

        # Test tex_coords list
        assert len(tex_coords) == 6
        assert len(tex_coords[0]) == 12

        # Test shading_values list
        assert len(shading_values) == 6
        assert len(shading_values[0]) == 4


# Run the test cases
if __name__ == '__main__':
    unittest.main()
