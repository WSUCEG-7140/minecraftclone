
import unittest
from soil import MinecraftSoil

class TestMinecraftSoil(unittest.TestCase):
    def setUp(self):
        self.soil = MinecraftSoil()

    def test_soil_properties(self):
        # Test transparency property
        self.assertTrue(self.soil.transparent)

        # Test transparency value
        self.assertEqual(self.soil.transparency, 2)

        # Test is_cube property
        self.assertFalse(self.soil.is_cube)

        # Test glass property
        self.assertFalse(self.soil.glass)

        # Test translucent property
        self.assertFalse(self.soil.translucent)

    def test_soil_data_structures(self):
        # Test colliders list
        self.assertEqual(len(self.soil.colliders), 1)
        self.assertEqual(len(self.soil.colliders[0]), 2)
        self.assertEqual(self.soil.colliders[0][0], (-0.5, -0.5000, -0.5))
        self.assertEqual(self.soil.colliders[0][1], (0.5,  0.4375,  0.5))

        # Test vertex_positions list
        self.assertEqual(len(self.soil.vertex_positions), 6)
        self.assertEqual(len(self.soil.vertex_positions[0]), 12)

        # Test tex_coords list
        self.assertEqual(len(self.soil.tex_coords), 6)
        self.assertEqual(len(self.soil.tex_coords[0]), 12)

        # Test shading_values list
        self.assertEqual(len(self.soil.shading_values), 6)
        self.assertEqual(len(self.soil.shading_values[0]), 4)

# test_code.py ends here

if __name__ == '__main__':
    unittest.main()
