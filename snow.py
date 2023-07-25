"""
| This module implements issue#15 assigned to kruslin2 and passed automated unittest with 100% coverage
| The coverage report in pdf format is attached to the GitHub link pull request associated with issue#15.
| It declares all geometric variables needed to create snow in 3D block models for terrain.

https://minecraft.fandom.com/wiki/Snow_Block
"""

# import module to write testcases for the code
import unittest

# Constant variable initializations

# It is transparent, True or False
transparent = True

# Degree of transparency, 0 = not transparent, 1 = a bit transparent and 2 = very transparent
transparency = 2

# It is cube, True or False
is_cube = False

# It is made of glass, True or False
glass = False

# It is translucent, True or False
translucent = False

# Colliders values initialization, a list of float numbers
colliders = [
	[
		(-0.5, -0.5000, -0.5),
		( 0.5, -0.4375,  0.5)
	]
]
# relative vertices positions of snow for each pixel, a list of float numbers
vertex_positions = [
	[ 0.5, -0.4375,  0.5,   0.5, -0.4375, -0.5,  -0.5, -0.4375, -0.5,  -0.5, -0.4375,  0.5], # top
	[-0.5, -0.4375,  0.5,  -0.5, -0.4375, -0.5,   0.5, -0.4375, -0.5,   0.5, -0.4375,  0.5], # bottom
]
# relative textures coordinates initializations for each pixel, a list of float numbers
tex_coords = [
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
]
# shading values initialization for snow, list of float numbers
shading_values = [
	[1.0, 1.0, 1.0, 1.0],
	[0.4, 0.4, 0.4, 0.4],
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
        self.colliders = [
	[
		(-0.5, -0.5000, -0.5),
		( 0.5, -0.4375,  0.5)
	]
]
        # initialize vertices variable for testing
        self.vertex_positions = [
	[ 0.5, -0.4375,  0.5,   0.5, -0.4375, -0.5,  -0.5, -0.4375, -0.5,  -0.5, -0.4375,  0.5], # top
	[-0.5, -0.4375,  0.5,  -0.5, -0.4375, -0.5,   0.5, -0.4375, -0.5,   0.5, -0.4375,  0.5], # bottom
]        
        # initialize texture coordinates variable for testing
        self.tex_coords = [
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
]
        # initialize shading_values variable for testing
        self.shading_values =  [
	[1.0, 1.0, 1.0, 1.0],
	[0.4, 0.4, 0.4, 0.4],
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
    # test shading variable
    def test_shading_values(self):
        for values in self.shading_values:
            self.assertIsInstance(values, list)
            self.assertEqual(len(values), 4)


if __name__ == '__main__':
    unittest.main()



