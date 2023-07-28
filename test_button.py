import unittest
from button import MinecraftButton

class MinecraftButtonTest(unittest.TestCase):
    def test_transparency(self):
        button = MinecraftButton()
        self.assertTrue(button.transparent, "Transparency should be set to True")

    def test_transparency_level(self):
        button = MinecraftButton()
        self.assertEqual(button.transparency, 2, "Transparency level should be 2")

    def test_is_cube(self):
        button = MinecraftButton()
        self.assertFalse(button.is_cube, "The button should not be a cube")

    def test_glass_material(self):
        button = MinecraftButton()
        self.assertFalse(button.glass, "The button should not be made of glass")

    def test_translucency(self):
        button = MinecraftButton()
        self.assertFalse(button.translucent, "The button should not be translucent")

    def test_colliders_empty(self):
        button = MinecraftButton()
        self.assertEqual(len(button.colliders), 0, "Colliders list should be empty")

    def test_vertex_positions(self):
        button = MinecraftButton()
        self.assertEqual(len(button.vertex_positions), 6, "Vertex positions should have 6 sets of coordinates")

    def test_tex_coords(self):
        button = MinecraftButton()
        self.assertEqual(len(button.tex_coords), 6, "Texture coordinates should have 6 sets of coordinates")

    def test_shading_values(self):
        button = MinecraftButton()
        self.assertEqual(len(button.shading_values), 6, "Shading values should have 6 sets of values")

    def test_set_properties(self):
        button = MinecraftButton()
        button.set_properties(False, 3, True, True, True, ["collider1", "collider2"])
        self.assertFalse(button.transparent, "Transparency should be set to False")
        self.assertEqual(button.transparency, 3, "Transparency level should be 3")
        self.assertTrue(button.is_cube, "The button should be a cube")
        self.assertTrue(button.glass, "The button should be made of glass")
        self.assertTrue(button.translucent, "The button should be translucent")
        self.assertEqual(len(button.colliders), 2, "Colliders list should have 2 elements")

if __name__ == '__main__':
    unittest.main()
