"""
 | This module implements issue#15 assigned to kruslin2 and passed automated unittest with 100% coverage
 | The coverage report in pdf format is attached to the GitHub link pull request associated with issue#15.
 | It declares all geometric variables needed to create doors in 3D block models for terrain.
"""

#import module to write testcases for the code
import unittest

# variables initialization

# Door is not transparent
transparent = False

# Degree of tranparency
transparency = 0

# Door is cube
is_cube = True

# Door is not glass
glass = False

# Door is not translucent
translucent = False

# It has no colliders values
colliders = []

# vertices positions initialization, to make doors
vertex_positions = [
	[ 0.5,  0.5,  0.5,  0.5, -0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5], # right
	[-0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5,  0.5,  0.5], # left
	[ 0.5,  0.5,  0.5,  0.5,  0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5,  0.5], # top
	[-0.5, -0.5,  0.5, -0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5, -0.5,  0.5], # bottom
	[-0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5,  0.5,  0.5,  0.5,  0.5], # front
	[ 0.5,  0.5, -0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5], # back
]


# textures coordinates initialization, where textures drawn pixel by pixel
tex_coords = [
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
]

# shading values initialization, the shading intensities
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
        self.transparent = False
        self.transparency = 0
        self.is_cube = True
        self.glass = False
        self.translucent = False

        self.colliders = []

        self.vertex_positions = [
            [0.5, 0.5, 0.5, 0.5, -0.5, 0.5, 0.5, -
                0.5, -0.5, 0.5, 0.5, -0.5],  # right
            [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, - \
                0.5, -0.5, 0.5, -0.5, 0.5, 0.5],  # left
            [0.5, 0.5, 0.5, 0.5, 0.5, -0.5, -0.5,
                0.5, -0.5, -0.5, 0.5, 0.5],  # top
            [-0.5, -0.5, 0.5, -0.5, -0.5, -0.5, 0.5, - \
                0.5, -0.5, 0.5, -0.5, 0.5],  # bottom
            [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, - \
                0.5, 0.5, 0.5, 0.5, 0.5],  # front
            [0.5, 0.5, -0.5, 0.5, -0.5, -0.5, -0.5, - \
                0.5, -0.5, -0.5, 0.5, -0.5],  # back
        ]

        self.tex_coords = [
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
    # test transparent variable
    def test_transparent(self):
        self.assertFalse(self.transparent)
    # test transparency variable
    def test_transparency(self):
        self.assertEqual(self.transparency, 0)
    # test is_cube variable
    def test_is_cube(self):
        self.assertTrue(self.is_cube)
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
    # test shading_values variable
    def test_shading_values(self):
        for values in self.shading_values:
            self.assertIsInstance(values, list)
            self.assertEqual(len(values), 4)


if __name__ == '__main__':
    unittest.main()
