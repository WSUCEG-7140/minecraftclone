
import unittest
from liquid import MinecraftLiquid

class TestMinecraftLiquid(unittest.TestCase):
    def setUp(self):
        self.liquid = MinecraftLiquid()

    def test_liquid_properties(self):
        # Test transparency property
        self.assertTrue(self.liquid.transparent)

        # Test transparency value
        self.assertEqual(self.liquid.transparency, 1)

        # Test is_cube property
        self.assertTrue(self.liquid.is_cube)

        # Test glass property
        self.assertTrue(self.liquid.glass)

        # Test translucent property
        self.assertTrue(self.liquid.translucent)

    def test_liquid_data_structures(self):
        # Test colliders list
        self.assertEqual(len(self.liquid.colliders), 0)

        # Test vertex_positions list
        self.assertEqual(len(self.liquid.vertex_positions), 6)
        self.assertEqual(len(self.liquid.vertex_positions[0]), 12)

        # Test tex_coords list
        self.assertEqual(len(self.liquid.tex_coords), 6)
        self.assertEqual(len(self.liquid.tex_coords[0]), 12)

        # Test shading_values list
        self.assertEqual(len(self.liquid.shading_values), 6)
        self.assertEqual(len(self.liquid.shading_values[0]), 4)


if __name__ == '__main__':
    unittest.main()
