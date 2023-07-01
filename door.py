#import module to write testcases for the code
import unittest

# variables declarations
transparent = False
transparency = 0
is_cube = True
glass = False
translucent = False

colliders = []

# vertices positions
vertex_positions = [
	[ 0.5,  0.5,  0.5,  0.5, -0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5], # right
	[-0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5,  0.5,  0.5], # left
	[ 0.5,  0.5,  0.5,  0.5,  0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5,  0.5], # top
	[-0.5, -0.5,  0.5, -0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5, -0.5,  0.5], # bottom
	[-0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5,  0.5,  0.5,  0.5,  0.5], # front
	[ 0.5,  0.5, -0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5], # back
]

# texture coordinates
tex_coords = [
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
]

# shading values
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
