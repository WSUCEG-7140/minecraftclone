import unittest
transparent = False
transparency = 0
translucent = False
is_cube = True
glass = False

//set values of colliders
colliders = [
	[
		(-0.5, -0.5, -0.5),
		( 0.5,  0.5,  0.5)
	]
]

//set values of vertex_positions
vertex_positions = [
	[ 0.5,  0.5,  0.5,  0.5, -0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5], # right
	[-0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5,  0.5,  0.5], # left
	[ 0.5,  0.5,  0.5,  0.5,  0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5,  0.5], # top
	[-0.5, -0.5,  0.5, -0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5, -0.5,  0.5], # bottom
	[-0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5,  0.5,  0.5,  0.5,  0.5], # front
	[ 0.5,  0.5, -0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5], # back
]

//set texture co-ordinates
tex_coords = [
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
]

//set shading values of the is_cube 
shading_values = [
	[0.6, 0.6, 0.6, 0.6],
	[0.6, 0.6, 0.6, 0.6],
	[1.0, 1.0, 1.0, 1.0],
	[0.4, 0.4, 0.4, 0.4],
	[0.8, 0.8, 0.8, 0.8],
	[0.8, 0.8, 0.8, 0.8],
]
class CubeTestCase(unittest.TestCase):
    def test_cube_properties(self):
        # Test transparency property
        self.assertFalse(transparent,"Transparency should be set to false")

        # Test transparency value
        self.assertEqual(transparency,0,"Transparency should be set to 0")

        # Test is_cube property
        self.assertTrue(is_cube, "is_cube should be set to true")

    def test_cube_data_structures(self):
        # Test colliders list
        assert len(colliders) == 1
        assert len(colliders[0]) == 2
        assert colliders[0][0] == (-0.5, -0.5, -0.5)
        assert colliders[0][1] == ( 0.5,  0.5,  0.5)

        # Test vertex_positions list
        assert len(vertex_positions) == 6
        assert len(vertex_positions[0]) == 12
        # Add more specific checks for each vertex position

        # Test tex_coords list
        assert len(tex_coords) == 6
        assert len(tex_coords[0]) == 12
        # Add more specific checks for each texture coordinate

        # Test shading_values list
        assert len(shading_values) == 6
        assert len(shading_values[0]) == 4

# Run the test cases
if __name__ == '__main__':
    unittest.main()

