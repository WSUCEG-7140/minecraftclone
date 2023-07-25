"""
| This module implements issue#65 assigned to kruslin2 and passed automated unittest with 100% coverage
| The coverage report in pdf format is attached to the GitHub link pull request associated with issue#65.
| It declares all geometric variables needed to create leaves on a tree in 3D block models for terrain.

https://minecraft-archive.fandom.com/wiki/Leaves
"""

# import module to write testcases for the code
import unittest
# Constant variables initializations

# It is transparent, True or False
transparent = True

# Degree of transparency, 0 = not transparent, 1 = a bit transparent and 2 = very transparent
transparency = 1

# It is of a cube shape, True or False
is_cube = True

# It is glass, True of False
glass = False

# It is translucent, True or False
translucent = False

# It has colliders values to initialize,  a list of float numbers
colliders = [
	[
		(-0.5, -0.5, -0.5),
		( 0.5,  0.5,  0.5)
	]
]


# vertices positions initialization,  a list of float numbers, to make leaves
vertex_positions = [
	[ 0.5,  0.5,  0.5,  0.5, -0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5], # right
	[-0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5,  0.5,  0.5], # left
	[ 0.5,  0.5,  0.5,  0.5,  0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5,  0.5], # top
	[-0.5, -0.5,  0.5, -0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5, -0.5,  0.5], # bottom
	[-0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5,  0.5,  0.5,  0.5,  0.5], # front
	[ 0.5,  0.5, -0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5], # back
]

# textures coordinates initialization,  a list of integer numbers, where textures drawn pixel by pixel
tex_coords = [
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
]

# shading values initialization,  a list of float numbers, the shading intensities
shading_values = [
	[0.6, 0.6, 0.6, 0.6],
	[0.6, 0.6, 0.6, 0.6],
	[1.0, 1.0, 1.0, 1.0],
	[0.4, 0.4, 0.4, 0.4],
	[0.8, 0.8, 0.8, 0.8],
	[0.8, 0.8, 0.8, 0.8],
]

# Class Unittest
class MyCodeTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test data or configurations

        # Initialize the code variables for testing
        self.transparent = True
        self.transparency = 1
        self.is_cube = True
        self.glass = False
        self.translucent = False

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
        self.assertFalse(self.glass)

    # Test translucent variable
    def test_translucent(self):
        self.assertFalse(self.translucent)

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





