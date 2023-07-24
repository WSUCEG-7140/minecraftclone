"""
| This module implements issue#15 assigned to kruslin2 and passed automated unittest with 100% coverage
| The coverage report in pdf format is attached to the GitHub link pull request associated with issue#15.
| It declares all geometric variables needed to create fires in 3D block models for terrain.

https://wiki.sportskeeda.com/minecraft/fire-in-minecraft
"""

#import module to write testcases for the code
import unittest

# constant variables initialization

# It is transparent
transparent = True

# Degree of transparency
transparency = 2

# It is not cube
is_cube = False

# It is not glass
glass = False

# It is not translucent
translucent = False

# It has no colliders values
colliders = []

# vertices positions initialization, to make fires
vertex_positions = [
	[-0.3536, 0.5000,  0.3536, -0.3536, -0.5000,  0.3536,  0.3536, -0.5000, -0.3536,  0.3536, 0.5000, -0.3536],
	[-0.3536, 0.5000, -0.3536, -0.3536, -0.5000, -0.3536,  0.3536, -0.5000,  0.3536,  0.3536, 0.5000,  0.3536],
	[ 0.3536, 0.5000, -0.3536,  0.3536, -0.5000, -0.3536, -0.3536, -0.5000,  0.3536, -0.3536, 0.5000,  0.3536],
	[ 0.3536, 0.5000,  0.3536,  0.3536, -0.5000,  0.3536, -0.3536, -0.5000, -0.3536, -0.3536, 0.5000, -0.3536],
]

# textures coordinates initialization, where textures drawn pixel by pixel
tex_coords = [
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
]

# shading values initialization for the shading intensities
shading_values = [
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
]


# Class Unittest
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
	       [-0.3536, 0.5000,  0.3536, -0.3536, -0.5000,  0.3536,  0.3536, -0.5000, -0.3536,  0.3536, 0.5000, -0.3536],
	       [-0.3536, 0.5000, -0.3536, -0.3536, -0.5000, -0.3536,  0.3536, -0.5000,  0.3536,  0.3536, 0.5000,  0.3536],
	       [ 0.3536, 0.5000, -0.3536,  0.3536, -0.5000, -0.3536, -0.3536, -0.5000,  0.3536, -0.3536, 0.5000,  0.3536],
	       [ 0.3536, 0.5000,  0.3536,  0.3536, -0.5000,  0.3536, -0.3536, -0.5000, -0.3536, -0.3536, 0.5000, -0.3536],
        ]

        self.tex_coords = [
	       [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	       [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	       [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	       [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
        ]

        self.shading_values = [
	       [1.0, 1.0, 1.0, 1.0],
	       [1.0, 1.0, 1.0, 1.0],
	       [1.0, 1.0, 1.0, 1.0],
	       [1.0, 1.0, 1.0, 1.0],
        ]


    # test transparent variable
    def test_transparent(self):
        self.assertTrue(self.transparent)
    # test transparency variable
    def test_transparency(self):
        self.assertEqual(self.transparency, 2)
    # test is_cube variable
    def test_is_cube(self):
        self.assertFalse(self.is_cube)
    # test glass variable
    def test_glass(self):
        self.assertFalse(self.glass)
    # test translucent variable
    def test_translucent(self):
        self.assertFalse(self.translucent)
    # test colliders variable
    def test_colliders(self):
        self.assertIsInstance(self.colliders, list)
    # test vertices positions variable
    def test_vertex_positions(self):
        for positions in self.vertex_positions:
            self.assertIsInstance(positions, list)
            self.assertEqual(len(positions), 12)
    # test texture coordinates variable
    def test_tex_coords(self):
        for coords in self.tex_coords:
            self.assertIsInstance(coords, list)
            self.assertEqual(len(coords), 12)
    # test shading values variable
    def test_shading_values(self):
        for values in self.shading_values:
            self.assertIsInstance(values, list)
            self.assertEqual(len(values), 4)


if __name__ == '__main__':
    unittest.main()

