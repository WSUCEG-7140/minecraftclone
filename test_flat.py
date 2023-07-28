import unittest
from flat import MinecraftFlat

class MinecraftCubeTest(unittest.TestCase):
    def test_transparency(self):
        flat = MinecraftFlat()
        self.assertTrue(flat.transparent, "Transparency should be set to True")

    def test_transparency_level(self):
        flat = MinecraftFlat()
        self.assertEqual(flat.transparency, 2, "Transparency level should be 2")

    def test_is_cube(self):
        flat = MinecraftFlat()
        self.assertFalse(flat.is_cube, "This should not be a cube")

    def test_glass_material(self):
        flat = MinecraftFlat()
        self.assertFalse(flat.glass, "This should not be made of glass")

    def test_translucency(self):
        flat = MinecraftFlat()
        self.assertFalse(flat.translucent, "This should not be translucent")

    def test_colliders_empty(self):
        flat = MinecraftFlat()
        self.assertEqual(len(flat.colliders), 0, "Colliders list should be 0")

    def test_vertex_positions(self):
        flat = MinecraftFlat()
        self.assertEqual(len(flat.vertex_positions), 2, "Vertex positions should have 2 sets of coordinates")
                             
    def test_tex_coords(self):
        flat = MinecraftFlat()
        self.assertEqual(len(flat.tex_coords), 2, "Texture coordinates should have 2 sets of coordinates")

    def test_shading_values(self):
        flat = MinecraftFlat()
        self.assertEqual(len(flat.shading_values), 2, "Shading values should have 2 sets of values")

    def test_set_properties(self):
        flat = MinecraftFlat()
        flat.set_properties(True, 2, False, False, False, [])
        self.assertTrue(flat.transparent, "Transparency should be set to True")
        self.assertEqual(flat.transparency, 2, "Transparency level should be 2")
        self.assertFalse(flat.is_cube, "This is not a cube")
        self.assertFalse(flat.glass, "This should not be made of glass")
        self.assertFalse(flat.translucent, "This should not be translucent")
        self.assertEqual(len(flat.colliders), 0, "Colliders list should have 2 elements")

if __name__ == '__main__':
    unittest.main()
