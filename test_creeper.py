import unittest
from creeper import cow

class TestCow(unittest.TestCase):
    def setUp(self):
        self.cow = cow()

    def test_toggle_transparency(self):
        self.assertTrue(self.cow.transparent)
        self.cow.toggle_transparency()
        self.assertFalse(self.cow.transparent)
        self.cow.toggle_transparency()
        self.assertTrue(self.cow.transparent)

    def test_toggle_cube(self):
        self.assertFalse(self.cow.is_cube)
        self.cow.toggle_cube()
        self.assertTrue(self.cow.is_cube)
        self.cow.toggle_cube()
        self.assertFalse(self.cow.is_cube)

    def test_toggle_glass(self):
        self.assertFalse(self.cow.glass)
        self.cow.toggle_glass()
        self.assertTrue(self.cow.glass)
        self.cow.toggle_glass()
        self.assertFalse(self.cow.glass)

    def test_add_collider(self):
        self.assertEqual(len(self.cow.colliders), 0)
        self.cow.add_collider("box")
        self.assertEqual(len(self.cow.colliders), 1)
        self.assertEqual(self.cow.colliders[0], "box")
        self.cow.add_collider("sphere")
        self.assertEqual(len(self.cow.colliders), 2)
        self.assertEqual(self.cow.colliders[1], "sphere")

if __name__ == '__main__':
    unittest.main()
