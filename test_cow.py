# test_code.py
import unittest
from cow import MinecraftCow

class TestMinecraftCow(unittest.TestCase):
    def setUp(self):
        self.cow = MinecraftCow()

    def test_cow_properties(self):
        # Test transparency property
        self.assertTrue(self.cow.transparent)

        # Test transparency value
        self.assertEqual(self.cow.transparency, 2)

        # Test is_cube property
        self.assertFalse(self.cow.is_cube)

        # Test glass property
        self.assertFalse(self.cow.glass)

        # Test translucent property
        self.assertFalse(self.cow.translucent)

    def test_cow_data_structures(self):
        # Test colliders list
        self.assertEqual(len(self.cow.colliders), 1)
        self.assertEqual(len(self.cow.colliders[0]), 2)
        self.assertEqual(self.cow.colliders[0][0], (-0.4375, -0.5, -0.4375))
        self.assertEqual(self.cow.colliders[0][1], (0.4375, 0.5, 0.4375))

        # Test vertex_positions list
        self.assertEqual(len(self.cow.vertex_positions), 6)
        self.assertEqual(len(self.cow.vertex_positions[0]), 12)

        # Test tex_coords list
        self.assertEqual(len(self.cow.tex_coords), 6)
        self.assertEqual(len(self.cow.tex_coords[0]), 12)

        # Test shading_values list
        self.assertEqual(len(self.cow.shading_values), 6)
        self.assertEqual(len(self.cow.shading_values[0]), 4)

# test_code.py ends here

if __name__ == '__main__':
    unittest.main()
