import unittest
import random
import math

import entity

class Mob(entity.Entity):
    def __init__(self, world, entity_type):
        super().__init__(world, entity_type)

        self.heading = 0
        self.select_target()

        self.reset()

    def select_target(self):
        self.target = [x + random.randint(-10, 10) for x in self.position]

    def update(self, delta_time):
        # Change target every 3 seconds on average
        if not random.randint(0, int(3 / delta_time)):
            self.select_target()

        delta_x = self.position[0] - self.target[0]
        delta_y = self.position[2] - self.target[2]

        self.heading = -math.atan2(delta_y, delta_x) + math.tau / 4
        self.heading += math.modf((self.rotation[0] - math.tau / 4) / math.tau)[1] * math.tau

        if delta_time * 5 > 1:
            self.rotation[0] = self.heading
        else:
            self.rotation[0] += (self.heading - self.rotation[0]) * delta_time * 5

        target_dist = math.sqrt(delta_x ** 2 + delta_y ** 2)

        if target_dist > 1:
            self.accel[0] =  math.cos(self.rotation[0] + math.tau / 4) * 3
            self.accel[2] = -math.sin(self.rotation[0] + math.tau / 4) * 3

        super().update(delta_time)

        # Check for collision with a wall and being on the ground
        if self.wall and self.grounded:
            if random.randint(0, 3):
                self.jump()
            else:
                self.select_target()

        if self.position[1] < 0:
            self.teleport((0, 80, 0))
#test cases
class MobTestCase(unittest.TestCase):
	def setUp(self):
		self.world = None
		self.entity_type = None
		self.mob = mob.Mob(self.world, self.entity_type)

	@patch.object(random, 'randint')
	def test_select_target(self, mock_randint):
		mock_randint.return_value = 5
		self.mob.position = [1, 2, 3]
		self.mob.select_target()
		self.assertEqual(self.mob.target, [6, 7, 8])
		mock_randint.assert_called_once_with(-10, 10)

	def test_update_heading(self):
		self.mob.position = [1, 2, 3]
		self.mob.target = [4, 5, 6]
		self.mob.update_heading()
		expected_heading = -math.atan2(3, -3) + math.tau / 4
		expected_heading += math.modf((self.mob.rotation[0] - math.tau / 4) / math.tau)[1] * math.tau
		self.assertEqual(self.mob.heading, expected_heading)

	@patch.object(random, 'randint')
	@patch.object(math, 'cos')
	@patch.object(math, 'sin')
	@patch.object(math, 'sqrt')
	def test_update_acceleration(self, mock_sqrt, mock_sin, mock_cos, mock_randint):
		self.mob.position = [1, 2, 3]
		self.mob.target = [4, 5, 6]
		mock_sqrt.return_value = 2
		mock_cos.return_value = 0.5
		mock_sin.return_value = -0.5
		mock_randint.return_value = 2
		self.mob.update_acceleration(0.1)
		self.assertEqual(self.mob.accel, [0.5 * 3, 0, -0.5 * 3])
		mock_sqrt.assert_called_once_with(18)
		mock_cos.assert_called_once_with(self.mob.rotation[0] + math.tau / 4)
		mock_sin.assert_called_once_with(self.mob.rotation[0] + math.tau / 4)
		mock_randint.assert_called_once_with(0, 3)

	@patch.object(random, 'randint')
	def test_update(self, mock_randint):
		mock_randint.return_value = 0
		self.mob.position = [1, 2, 3]
		self.mob.target = [4, 5, 6]
		self.mob.rotation = [0, 0, 0]
		self.mob.wall = True
		self.mob.grounded = True
		self.mob.jump = lambda: None
		self.mob.select_target = lambda: None
		self.mob.update(0.1)
		self.assertEqual(self.mob.rotation[0], self.mob.heading)
		self.mob.jump.assert_not_called()
		self.mob.select_target.assert_called_once()

	def test_update_below_ground(self):
		self.mob.position = [1, -1, 3]
		self.mob.teleport = lambda pos: None
		self.mob.update(0.1)
		self.mob.teleport.assert_called_once_with((0, 80, 0))

if __name__ == '__main__':
	unittest.main()
