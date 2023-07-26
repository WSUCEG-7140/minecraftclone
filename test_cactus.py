# Import the unittest module and the MineCraftCactus class from cactus.py
import unittest
from cactus import MineCraftCactus

# Define a test class TestMineCraftCactus that inherits from unittest.TestCase
class TestMineCraftCactus(unittest.TestCase):
    # Define a setUp method that will be called before each test method
    def setUp(self):
        # Create an instance of the MineCraftCactus class and store it in the variable 'cactus'
        self.cactus = MineCraftCactus()

        # Initialize the colliders, vertex_positions, tex_coords, and shading_values data structures for the cactus
        self.cactus.initialize_colliders()
        self.cactus.initialize_vertex_positions()
        self.cactus.initialize_tex_coords()
        self.cactus.initialize_shading_values()

    # Define a test method test_cactus_properties to test the properties of the cactus
    def test_cactus_properties(self):
        # Test that the 'transparent' property of the cactus is True
        self.assertTrue(self.cactus.properties['transparent'], "Transparency should be set to true")

        # Test that the 'transparency' property of the cactus is equal to 2
        self.assertEqual(self.cactus.properties['transparency'], 2, "Transparency should be set to 2")

        # Test that the 'is_cube' property of the cactus is False
        self.assertFalse(self.cactus.properties['is_cube'], "is_cube should be set to false")

    # Define a test method test_cactus_data_structures to test the data structures of the cactus
    def test_cactus_data_structures(self):
        # Test the 'colliders' list of the cactus
        self.assertEqual(len(self.cactus.colliders), 1, "Number of colliders should be 1")
        self.assertEqual(len(self.cactus.colliders[0]), 2, "Number of collider bounds should be 2")
        self.assertEqual(self.cactus.colliders[0][0], (-0.4375, -0.5, -0.4375), "Invalid collider lower bound")
        self.assertEqual(self.cactus.colliders[0][1], (0.4375, 0.5, 0.4375), "Invalid collider upper bound")

        # Test the 'vertex_positions' list of the cactus
        self.assertEqual(len(self.cactus.vertex_positions), 6, "Number of vertex positions lists should be 6")
        self.assertEqual(len(self.cactus.vertex_positions[0]), 12, "Number of vertex positions for a face should be 12")
        # Add more specific checks for each vertex position

        # Test the 'tex_coords' list of the cactus
        self.assertEqual(len(self.cactus.tex_coords), 6, "Number of texture coordinate lists should be 6")
        self.assertEqual(len(self.cactus.tex_coords[0]), 12, "Number of texture coordinates for a face should be 12")
        # Add more specific checks for each texture coordinate

        # Test the 'shading_values' list of the cactus
        self.assertEqual(len(self.cactus.shading_values), 6, "Number of shading values lists should be 6")
        self.assertEqual(len(self.cactus.shading_values[0]), 4, "Number of shading values for a face should be 4")

# Check if the script is being run as the main module, and run the unittests if it is
if __name__ == '__main__':
    unittest.main()
