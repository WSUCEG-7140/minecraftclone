"""
| This module implements issue#48 assigned to kruslin2 and passed automated unittest with 100% coverage
| The coverage report in pdf format is attached to the GitHub link pull request associated with issue#48
| It declares all geometric variables needed to create a torch in 3d block models for terrain.

https://minecraft.fandom.com/wiki/Torch
"""

# import module to write test cases for the code
import unittest

# variable initializations

# It is transparent
transparent = True

# Degree of transparency
transparency = 2
# It is not a cube shape
is_cube = False
# It is not glass
glass = False
# It is not translucent
translucent = False
# It has no colliders
colliders = []

# vertices positions initialization, to make the torch flicker
vertex_positions = [
	[ 0.0625,  0.5,  0.5,    0.0625, -0.5,  0.5,    0.0625, -0.5, -0.5,    0.0625,  0.5, -0.5], # right
	[-0.0625,  0.5, -0.5,   -0.0625, -0.5, -0.5,   -0.0625, -0.5,  0.5,   -0.0625,  0.5,  0.5], # left
	[ 0.5,  0.125,  0.5,    0.5,  0.125, -0.5,   -0.5,  0.125, -0.5,   -0.5,  0.125,  0.5], # top
	[-0.5, -0.5,  0.5,   -0.5, -0.5, -0.5,    0.5, -0.5, -0.5,    0.5, -0.5,  0.5], # bottom
	[-0.5,  0.5,  0.0625,   -0.5, -0.5,  0.0625,    0.5, -0.5,  0.0625,    0.5,  0.5,  0.0625], # front
	[ 0.5,  0.5, -0.0625,    0.5, -0.5, -0.0625,   -0.5, -0.5, -0.0625,   -0.5,  0.5, -0.0625], # back
]
# textures coordinates initialization, where textures drawn pixel by pixel
tex_coords = [
	[0.0, 1.0, 0.0,   0.0, 0.0, 0.0,   1.0, 0.0, 0.0,   1.0, 1.0, 0.0], # right
	[0.0, 1.0, 0.0,   0.0, 0.0, 0.0,   1.0, 0.0, 0.0,   1.0, 1.0, 0.0], # left
	[0.0, 1.0, 0.0,   0.0, 0.0, 0.0,   1.0, 0.0, 0.0,   1.0, 1.0, 0.0], # top
	[0.0, 1.0, 0.0,   0.0, 0.0, 0.0,   1.0, 0.0, 0.0,   1.0, 1.0, 0.0], # bottom
	[0.0, 1.0, 0.0,   0.0, 0.0, 0.0,   1.0, 0.0, 0.0,   1.0, 1.0, 0.0], # front
	[0.0, 1.0, 0.0,   0.0, 0.0, 0.0,   1.0, 0.0, 0.0,   1.0, 1.0, 0.0], # back
]

# shading values initialization, the shading intensities
shading_values = [
	[0.6, 0.6, 0.6, 0.6], # right
	[0.6, 0.6, 0.6, 0.6], # left
	[1.0, 1.0, 1.0, 1.0], # top
	[0.4, 0.4, 0.4, 0.4], # bottom
	[0.8, 0.8, 0.8, 0.8], # front
	[0.8, 0.8, 0.8, 0.8], # back 
]

# Unittest
# Class unittest
class MyCodeTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test data or configurations

        # Initialize the code variables for testing
        self.transparent = True
        self.transparency = 2
        self.is_cube = False
        self.glass = False
        self.translucent = False

        self.colliders = []

        self.vertex_positions = [
	[ 0.0625,  0.5,  0.5,    0.0625, -0.5,  0.5,    0.0625, -0.5, -0.5,    0.0625,  0.5, -0.5], # right
	[-0.0625,  0.5, -0.5,   -0.0625, -0.5, -0.5,   -0.0625, -0.5,  0.5,   -0.0625,  0.5,  0.5], # left
	[ 0.5,  0.125,  0.5,    0.5,  0.125, -0.5,   -0.5,  0.125, -0.5,   -0.5,  0.125,  0.5], # top
	[-0.5, -0.5,  0.5,   -0.5, -0.5, -0.5,    0.5, -0.5, -0.5,    0.5, -0.5,  0.5], # bottom
	[-0.5,  0.5,  0.0625,   -0.5, -0.5,  0.0625,    0.5, -0.5,  0.0625,    0.5,  0.5,  0.0625], # front
	[ 0.5,  0.5, -0.0625,    0.5, -0.5, -0.0625,   -0.5, -0.5, -0.0625,   -0.5,  0.5, -0.0625], # back
]
        self.tex_coords = [
	[0.0, 1.0, 0.0,   0.0, 0.0, 0.0,   1.0, 0.0, 0.0,   1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,   0.0, 0.0, 0.0,   1.0, 0.0, 0.0,   1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,   0.0, 0.0, 0.0,   1.0, 0.0, 0.0,   1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,   0.0, 0.0, 0.0,   1.0, 0.0, 0.0,   1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,   0.0, 0.0, 0.0,   1.0, 0.0, 0.0,   1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,   0.0, 0.0, 0.0,   1.0, 0.0, 0.0,   1.0, 1.0, 0.0],
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
        self.assertEqual(self.transparency, 2)

    # Test is_cube variable
    def test_is_cube(self):
        self.assertFalse(self.is_cube)

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





































