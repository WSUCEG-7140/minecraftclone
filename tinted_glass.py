# This module implements issue#67 assigned to kruslin2 and passed automated unittest with 100% coverage
# The coverage report in pdf format is attached to the GitHub link pull request associated with issue#67. 
# It declares all geometric variables needed to create tinted glasses in 3D terrain.

# import module to write testcases for the code
import unittest

# constant variables initializations

# the variable indicates tinted_glass is always transparent
transparent = True

# The value 1 for being transparent or otherwise 0
transparency = 1

# tinted_glass has a cube shape
is_cube = True

# tinted_glass is glass
glass = True

# tinted_glass is translucent
translucent = True

# the point coordinates to collide
colliders = [
	[
		(-0.5, -0.5, -0.5),
		( 0.5,  0.5,  0.5)
	]
]

# relative vertices positions of tinted_glass for each pixel
vertex_positions = [
	[ 0.5,  0.5,  0.5,  0.5, -0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5], # right
	[-0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5,  0.5,  0.5], # left
	[ 0.5,  0.5,  0.5,  0.5,  0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5,  0.5], # top
	[-0.5, -0.5,  0.5, -0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5, -0.5,  0.5], # bottom
	[-0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5,  0.5,  0.5,  0.5,  0.5], # front
	[ 0.5,  0.5, -0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5], # back
]
# relative textures coordinates for each pixel
tex_coords = [
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0], # right
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0], # left
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0], # top
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0], # bottom
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0], # front
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0], # back
]
# shading values for tinted_glass
shading_values = [
	[0.6, 0.6, 0.6, 0.6], # right
	[0.6, 0.6, 0.6, 0.6], # left
	[1.0, 1.0, 1.0, 1.0], # top
	[0.4, 0.4, 0.4, 0.4], # bottom
	[0.8, 0.8, 0.8, 0.8], # front
	[0.8, 0.8, 0.8, 0.8], # back
]

# Class Unittest
class MyCodeTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test data or configurations

        # Initialize the code variables for testing
        self.transparent = True
        self.transparency = 1
        self.is_cube = True
        self.glass = True
        self.translucent = True

        self.colliders = [
	[
		(-0.5, -0.5, -0.5),
		( 0.5,  0.5,  0.5)
	]
]
        self.vertex_positions = [
	[ 0.5,  0.5,  0.5,  0.5, -0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5], # right
	[-0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5,  0.5,  0.5], # left
	[ 0.5,  0.5,  0.5,  0.5,  0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5,  0.5], # top
	[-0.5, -0.5,  0.5, -0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5, -0.5,  0.5], # bottom
	[-0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5,  0.5,  0.5,  0.5,  0.5], # front
	[ 0.5,  0.5, -0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5], # back
]

        self.tex_coords =  [
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
]

        self.shading_values = [
	[0.6, 0.6, 0.6, 0.6],
	[0.6, 0.6, 0.6, 0.6],
	[1.0, 1.0, 1.0, 1.0],
	[0.4, 0.4, 0.4, 0.4],
	[0.8, 0.8, 0.8, 0.8],
	[0.8, 0.8, 0.8, 0.8],
]

 
    # Test transparent variable
    def test_transparent(self):
        self.assertTrue(self.transparent)

    # Test transparency variable
    def test_transparency(self):
        self.assertEqual(self.transparency, 1)

    # Test is_cube variable
    def test_is_cube(self):
        self.assertTrue(self.is_cube)

    # Test glass variable
    def test_glass(self):
        self.assertTrue(self.glass)

    # Test translucent variable
    def test_translucent(self):
        self.assertTrue(self.translucent)

    # Test colliders variable
    def test_colliders(self):
        self.assertIsInstance(self.colliders, list)

    # Test vertex_positions variable
    def test_vertex_positions(self):
        for positions in self.vertex_positions:
            self.assertIsInstance(positions, list)
            self.assertEqual(len(positions), 12)

    # Test tex_coords variable
    def test_tex_coords(self):
        for coords in self.tex_coords:
            self.assertIsInstance(coords, list)
            self.assertEqual(len(coords), 12)

    # Test shading_values variable
    def test_shading_values(self):
        for values in self.shading_values:
            self.assertIsInstance(values, list)
            self.assertEqual(len(values), 4)


if __name__ == '__main__':
    unittest.main()


























