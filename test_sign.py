import unittest
from sign import MinecraftSign

class TestMinecraftSign(unittest.TestCase):
    def setUp(self):
        self.sign = MinecraftSign()

    def test_sign_properties(self):
        # Test transparency property
        self.assertTrue(self.sign.transparent)

        # Test transparency value
        self.assertEqual(self.sign.transparency, 2)

        # Test is_cube property
        self.assertFalse(self.sign.is_cube)

        # Test glass property
        self.assertFalse(self.sign.glass)

        # Test translucent property
        self.assertFalse(self.sign.translucent)

    def test_sign_data_structures(self):
        # Test colliders list
        self.assertEqual(len(self.sign.colliders), 0)

        # Test vertex_positions list
        self.assertEqual(len(self.sign.vertex_positions), 4)
        self.assertEqual(len(self.sign.vertex_positions[0]), 12)

        # Test tex_coords list
        self.assertEqual(len(self.sign.tex_coords), 4)
        self.assertEqual(len(self.sign.tex_coords[0]), 12)

        # Test shading_values list
        self.assertEqual(len(self.sign.shading_values), 4)
        self.assertEqual(len(self.sign.shading_values[0]), 4)


if __name__ == '__main__':
    unittest.main()
