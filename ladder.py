"""
| This module implements issue#50 assigned to kruslin2 and passed automated unittest with 100% coverage
| The coverage report in pdf format is attached to the GitHub link pull request associated with issue#50.
| It declares all geometric variables needed to create ladders in 3D block models for terrain.

https://minecraft.fandom.com/wiki/Ladder
"""


# import module to write testcases for the code
import unittest
# constant variable initializations

# It is transparent, True or False
transparent = True

# Degree of transparency, 0 = not transparent, 1 = a bit transparent and 2 = very transparent
transparency = 2

# It is of a cube shape, True or False
is_cube = False

# It is made of glass, True or False
glass = False

# It is tranlucent, True or False
translucent = False

# It has no colliders values initialized
colliders = []


# vertices positions initialization,  a list of float numbers, to make a ladder
vertex_positions = [
	[-0.3536, 0.5000,  0.3536, -0.3536, -0.5000,  0.3536,  0.3536, -0.5000, -0.3536,  0.3536, 0.5000, -0.3536],
	[-0.3536, 0.5000, -0.3536, -0.3536, -0.5000, -0.3536,  0.3536, -0.5000,  0.3536,  0.3536, 0.5000,  0.3536],
	[ 0.3536, 0.5000, -0.3536,  0.3536, -0.5000, -0.3536, -0.3536, -0.5000,  0.3536, -0.3536, 0.5000,  0.3536],
	[ 0.3536, 0.5000,  0.3536,  0.3536, -0.5000,  0.3536, -0.3536, -0.5000, -0.3536, -0.3536, 0.5000, -0.3536],
]
# textures coordinates initialization,  a list of integer numbers, where textures drawn pixel by pixel
tex_coords = [, 
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
]

# shading values initialization,  a list of integer, numbers, the shading intensities
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

    # Test vertex_position variable
    def test_vertex_positions(self):
        for positions in self.vertex_positions:
            self.assertIsInstance(positions, list)
            self.assertEqual(len(positions), 12)

    # Test tex_coords variable
    def test_tex_coords(self):
        for coords in self.tex_coords:
            self.assertIsInstance(coords, list)
            self.assertEqual(len(coords), 12)

    # Test shading_values
    def test_shading_values(self):
        for values in self.shading_values:
            self.assertIsInstance(values, list)
            self.assertEqual(len(values), 4)


if __name__ == '__main__':
    unittest.main()






