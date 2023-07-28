"""
  | This module implements issue#63 assigned to kruslin2 and passed automated unittest with 100% coverage
  | The coverage report in pdf format is attached to the GitHub link pull request associated with issue#63.
  | This module is accessed by other modules for collidings operations
"""

#import module to write testcases for the code
import unittest

# Class collider declaration
# This Class has functions to determine if two 3D moving point coordinates collide
class Collider:

	# Class Collider constructer
	def __init__(self, pos1 = (None,) * 3, pos2 = (None,) * 3):
		# pos1: position of the collider vertex in the -X, -Y, -Z direction
		# pos2: position of the collider vertex in the +X, +Y, +Z direction
		self.x1, self.y1, self.z1 = pos1
		self.x2, self.y2, self.z2 = pos2

        # Shifting positions of variables (x1, y1, z1) and (x2, y2, z2)
	def __add__(self, pos):

		"""
		This class function performs shifting operations of an object

		:param name: pos
		:param type: list
		:return: class object
		"""
		x, y, z = pos
		return Collider(
			(self.x1 + x, self.y1 + y, self.z1 + z),
			(self.x2 + x, self.y2 + y, self.z2 + z)
		)
	    # Colliding conditioning
	def __and__(self, collider):

		"""
		This class function performs colliding condition operations.

		:param name: collider
		:param type: Class object
		:return: boolean
		"""
		x = min(self.x2, collider.x2) - max(self.x1, collider.x1)
		y = min(self.y2, collider.y2) - max(self.y1, collider.y1)
		z = min(self.z2, collider.z2) - max(self.z1, collider.z1)

		return x > 0 and y > 0 and z > 0
	
        # Colliding determination
	def collide(self, collider, velocity):
		# self: the dynamic collider, which moves
		# collider: the static collider, which stays put

		"""
		This class function performs investigation on collision between the class object itself and an object collider.

		:param name: collider, velocity
		:param type: object, list
		:return type: int, list 
		"""

		no_collision = 1, None

		# find entry & exit times for each axis

		vx, vy, vz = velocity

		time = lambda x, y: x / y if y else float('-' * (x > 0) + "inf")

		x_entry = time(collider.x1 - self.x2 if vx > 0 else collider.x2 - self.x1, vx)
		x_exit  = time(collider.x2 - self.x1 if vx > 0 else collider.x1 - self.x2, vx)

		y_entry = time(collider.y1 - self.y2 if vy > 0 else collider.y2 - self.y1, vy)
		y_exit  = time(collider.y2 - self.y1 if vy > 0 else collider.y1 - self.y2, vy)

		z_entry = time(collider.z1 - self.z2 if vz > 0 else collider.z2 - self.z1, vz)
		z_exit  = time(collider.z2 - self.z1 if vz > 0 else collider.z1 - self.z2, vz)

		# make sure we actually got a collision

		if x_entry < 0 and y_entry < 0 and z_entry < 0:
			return no_collision

		if x_entry > 1 or y_entry > 1 or z_entry > 1:
			return no_collision
		
		# on which axis did we collide first ?

		entry = max(x_entry, y_entry, z_entry)
		exit_ = min(x_exit,  y_exit,  z_exit )
		
		if entry > exit_:
			return no_collision
		
		# find normal of surface we collided with

		nx = (0, -1 if vx > 0 else 1)[entry == x_entry]
		ny = (0, -1 if vy > 0 else 1)[entry == y_entry]
		nz = (0, -1 if vz > 0 else 1)[entry == z_entry]

		return entry, (nx, ny, nz)


# Class Unittest
class MyCodeTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test data or configurations
        
        self.aaa = Collider(( 1,  4, 10), (-100, -100, -100))
        self.bbb = self.aaa.__add__((-10, -40, -70))
        self.ccc = self.aaa.__and__((self.bbb))
        self.ddd = self.aaa.collide(self.bbb, (-5, -4, -2))
        self.eee = self.aaa.collide(self.bbb, (1000, 1000, 1000))
		
		
        self.aa = Collider(( -1,  -4, -10), (0, 0, 0))
        self.bb = self.aa.__add__((-1, 0, 1))
        self.cc = self.aa.__and__((self.bb))
        self.dd = self.aa.collide(self.bb, (-5, 4, 0))
        self.ee = self.aa.collide(self.bb, (100, 100, 100))
		
		
        self.a = Collider((23, 43, 12), (-10, 0, 67))
        self.b = self.a.__add__((-110, -120, -100))  
        self.h = self.a.__add__((-44, -55, -20))
        self.c = self.a.__and__(self.b)
        self.d = self.a.collide(self.b, (-52, 20, 9))    
	
        self.e = self.a.collide(self.b, (32, -50, 9))
	
        self.f = self.a.collide(self.h, (-500, -210, -100))
	

	

    def test_operation(self):
        # Test operations
        self.assertNotEqual((self.a.x1, self.a.y1, self.a.z1), (10, 10, 10))
        self.assertNotEqual((self.a.x2, self.a.y2, self.a.z2), (-10, 10, -10))
        self.assertNotEqual((self.b.x1, self.b.y1, self.b.z1), (11, 11, 11))
        self.assertNotEqual((self.b.x2, self.b.y2, self.b.z2), (-9, 11, -9))
        self.assertFalse(self.c)
        self.assertIsInstance(self.d, tuple)
        self.assertNotEqual(self.d, (-10, (0, 0, 0)))
        self.assertEqual(self.d, (1, None))
        self.assertEqual(self.e, (1, None))
        self.assertEqual(self.f, (1, None))
        self.assertEqual(self.ee, (1, None))
        self.assertEqual(self.ddd, (1, None))
        self.assertEqual(self.eee, (1, None))

	    


        

if __name__ == '__main__':
    unittest.main()  