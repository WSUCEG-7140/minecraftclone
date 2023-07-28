import unittest
from zombie import MinecraftZombie

class MinecraftZombieTester(unittest.TestCase):
    def setUp(self):
        self.zombie = MinecraftZombie()

    def test_transparent(self):
        assert self.zombie.transparent is True

    def test_is_cube(self):
        assert self.zombie.is_cube is False

    def test_glass(self):
        assert self.zombie.glass is False

    def test_colliders(self):
        assert isinstance(self.zombie.colliders, list)

    def test_bones(self):
        assert isinstance(self.zombie.bones, list)
        for bone in self.zombie.bones:
            assert isinstance(bone, dict)
            assert 'name' in bone
            assert 'pivot' in bone
            assert 'vertices' in bone
            assert 'tex_coords' in bone
            assert 'shading_values' in bone

if __name__ == "__main__":
    unittest.main()

