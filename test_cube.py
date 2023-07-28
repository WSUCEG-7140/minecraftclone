import unittest
from cube import MinecraftCube

class MinecraftCubeTest(unittest.TestCase):
    def test_transparency(self):
        cube = MinecraftCube()
        self.assertFalse(cube.transparent, "Transparency should be set to False")

    def test_transparency_level(self):
        cube = MinecraftCube()
        self.assertEqual(cube.transparency, 0, "Transparency level should be 0")

    def test_is_cube(self):
        cube = MinecraftCube()
        self.assertTrue(cube.is_cube, "This should be a cube")

    def test_glass_material(self):
        cube = MinecraftCube()
        self.assertFalse(cube.glass, "This should not be made of glass")

    def test_translucency(self):
        cube = MinecraftCube()
        self.assertFalse(cube.translucent, "This should not be translucent")

    def test_colliders_empty(self):
        cube = MinecraftCube()
        self.assertEqual(len(cube.colliders), 1, "Colliders list should be 1")

    def test_vertex_positions(self):
        cube = MinecraftCube()
        self.assertEqual(len(cube.vertex_positions), 6, "Vertex positions should have 6 sets of coordinates")
                             
    def test_tex_coords(self):
        cube = MinecraftCube()
        self.assertEqual(len(cube.tex_coords), 6, "Texture coordinates should have 6 sets of coordinates")

    def test_shading_values(self):
        cube = MinecraftCube()
        self.assertEqual(len(cube.shading_values), 6, "Shading values should have 6 sets of values")

    def test_set_properties(self):
        cube = MinecraftCube()
        cube.set_properties(False, 0, True, False, False, ["collider1", "collider2"])
        self.assertFalse(cube.transparent, "Transparency should be set to False")
        self.assertEqual(cube.transparency, 0, "Transparency level should be 0")
        self.assertTrue(cube.is_cube, "This a cube")
        self.assertFalse(cube.glass, "This should not be made of glass")
        self.assertFalse(cube.translucent, "This should not be translucent")
        self.assertEqual(len(cube.colliders), 2, "Colliders list should have 2 elements")

if __name__ == '__main__':
    unittest.main()
