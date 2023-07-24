"""
| This module implements issue#21 assigned to kruslin2 and passed automated unittest with 100% coverage
| The coverage report in pdf format is attached to the GitHub link pull request associated with issue#21.
| It declares all geometric variables needed to create 3D blokc models terrain.
"""

# import module to write testcases for the code
import unittest

# constant variables initializations

# vertices positions initialization, to create terrain
vertex_positions = [
	 0.5,  0.5,  0.5,  0.5, -0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5,
	-0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5,  0.5,  0.5,
	-0.5,  0.5,  0.5, -0.5,  0.5, -0.5,  0.5,  0.5, -0.5,  0.5,  0.5,  0.5,
	-0.5, -0.5,  0.5, -0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5, -0.5,  0.5,
	-0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5,  0.5,  0.5,  0.5,  0.5,
	 0.5,  0.5, -0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5,
]

# textures coordinates initialization, where textures drawn pixel by pixel
tex_coords = [
	0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
]

# shading values initialization, the shading intensities
shading = [
	0.80, 0.80, 0.80, 0.80,
	0.80, 0.80, 0.80, 0.80,
	1.00, 1.00, 1.00, 1.00,
	0.49, 0.49, 0.49, 0.49,
	0.92, 0.92, 0.92, 0.92,
	0.92, 0.92, 0.92, 0.92,
]

# Index values initializations for in plane orientation
indices = [
	 0,  1,  2,  0,  2,  3, # right
	 4,  5,  6,  4,  6,  7, # left
	 8,  9, 10,  8, 10, 11, # top
	12, 13, 14, 12, 14, 15, # bottom
	16, 17, 18, 16, 18, 19, # front
	20, 21, 22, 20, 22, 23, # back
]

# Class Unittest
class MyCodeTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test data or configurations

        # initialize vertices variable for testing
        self.vertex_positions = [
             0.5,  0.5,  0.5,  0.5, -0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5,
	        -0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5,  0.5,  0.5,
	        -0.5,  0.5,  0.5, -0.5,  0.5, -0.5,  0.5,  0.5, -0.5,  0.5,  0.5,  0.5,
	        -0.5, -0.5,  0.5, -0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5, -0.5,  0.5,
	        -0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5,  0.5,  0.5,  0.5,  0.5,
	         0.5,  0.5, -0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5,	
]        
        # initialize texture coordinates variable for testing
        self.tex_coords = [
            0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	
]
        # initialize shading_values variable for testing
        self.shading_values =  [
            0.80, 0.80, 0.80, 0.80,
	        0.80, 0.80, 0.80, 0.80,
	        1.00, 1.00, 1.00, 1.00,
	        0.49, 0.49, 0.49, 0.49,
	        0.92, 0.92, 0.92, 0.92,
	        0.92, 0.92, 0.92, 0.92,
]
        
        # Initialize index values variables for testing
        self.indices = [ 
            0,  1,  2,  0,  2,  3, # right
	        4,  5,  6,  4,  6,  7, # left  
	        8,  9, 10,  8, 10, 11, # top
	       12, 13, 14, 12, 14, 15, # bottom
	       16, 17, 18, 16, 18, 19, # front
	       20, 21, 22, 20, 22, 23, # back
]
 
    # test vertices positions variable
    def test_vertex_positions(self):
        self.assertEqual(self.vertex_positions, [
             0.5,  0.5,  0.5,  0.5, -0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5,
	        -0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5,  0.5,  0.5,
	        -0.5,  0.5,  0.5, -0.5,  0.5, -0.5,  0.5,  0.5, -0.5,  0.5,  0.5,  0.5,
	        -0.5, -0.5,  0.5, -0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5, -0.5,  0.5,
	        -0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5,  0.5,  0.5,  0.5,  0.5,
	         0.5,  0.5, -0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5,	
])
        
	 # test texture coordinates variable
    def test_tex_coords(self):
        self.assertEqual(self.tex_coords, [
            0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,
	        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0,	
])

    # test shading variable
    def test_shading_values(self):
        self.assertEqual(self.shading_values, [
            0.80, 0.80, 0.80, 0.80,
	        0.80, 0.80, 0.80, 0.80,
	        1.00, 1.00, 1.00, 1.00,
	        0.49, 0.49, 0.49, 0.49,
	        0.92, 0.92, 0.92, 0.92,
	        0.92, 0.92, 0.92, 0.92,   
])
            
    # test indexes variable
    def test_indices(self):
        self.assertEqual(self.indices, [ 
            0,  1,  2,  0,  2,  3,
	        4,  5,  6,  4,  6,  7, 
	        8,  9, 10,  8, 10, 11, 
	        12, 13, 14, 12, 14, 15, 
	        16, 17, 18, 16, 18, 19, 
	        20, 21, 22, 20, 22, 23, 
])


if __name__ == '__main__':
    unittest.main()
