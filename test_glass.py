
import unittest
from glass import MinecraftGlass

class TestMinecraftCow(unittest.TestCase):
    def setUp(self):
        self.glass = MinecraftGlass()

    def test_cow_properties(self):
        # Test transparency property
        self.assertTrue(self.glass.transparent)

        # Test transparency value
        self.assertEqual(self.glass.transparency, 2)

        # Test is_cube property
        self.assertTrue(self.glass.is_cube)

        # Test glass property
        self.assertTrue(self.glass.glass)

        # Test translucent property
        self.assertFalse(self.glass.translucent)

    def test_cow_data_structures(self):
        # Test colliders list
        self.assertEqual(len(self.glass.colliders), 1)
        self.assertEqual(len(self.glass.colliders[0]), 2)
        self.assertEqual(self.glass.colliders[0][0], (-0.5, -0.5, -0.5))
        self.assertEqual(self.glass.colliders[0][1], (0.5,  0.5,  0.5))

        # Test vertex_positions list
        self.assertEqual(len(self.glass.vertex_positions), 6)
        self.assertEqual(len(self.glass.vertex_positions[0]), 12)

        # Test tex_coords list
        self.assertEqual(len(self.glass.tex_coords), 6)
        self.assertEqual(len(self.glass.tex_coords[0]), 12)

        # Test shading_values list
        self.assertEqual(len(self.glass.shading_values), 6)
        self.assertEqual(len(self.glass.shading_values[0]), 4)

# test_code.py ends here

if __name__ == '__main__':
    unittest.main()
