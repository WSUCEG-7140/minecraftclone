import unittest
from skeleton import MinecraftSkeleton

class TestMinecraftSkeleton(unittest.TestCase):

    def test_transparency(self):
        skeleton = MinecraftSkeleton()
        self.assertTrue(skeleton.transparent)

    def test_is_cube(self):
        skeleton = MinecraftSkeleton()
        self.assertFalse(skeleton.is_cube)

    def test_glass(self):
        skeleton = MinecraftSkeleton()
        self.assertFalse(skeleton.glass)

    def test_colliders(self):
        skeleton = MinecraftSkeleton()
        self.assertEqual(len(skeleton.colliders), 0)

    def test_bones(self):
        skeleton = MinecraftSkeleton()
        self.assertEqual(len(skeleton.bones), 7)

    def test_bone_names(self):
        skeleton = MinecraftSkeleton()
        bone_names = [bone['name'] for bone in skeleton.bones]
        self.assertListEqual(bone_names, ['body', 'head', 'hat', 'rightArm', 'leftArm', 'rightLeg', 'leftLeg'])

    def test_bone_vertices(self):
        skeleton = MinecraftSkeleton()
        for bone in skeleton.bones:
            self.assertEqual(len(bone['vertices']), 6)

    def test_bone_tex_coords(self):
        skeleton = MinecraftSkeleton()
        for bone in skeleton.bones:
            self.assertEqual(len(bone['tex_coords']), 6)

    def test_bone_shading_values(self):
        skeleton = MinecraftSkeleton()
        for bone in skeleton.bones:
            self.assertEqual(len(bone['shading_values']), 6)

if __name__ == '__main__':
    unittest.main()
