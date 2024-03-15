import unittest
from mathmanager import mathmanager

class mathmanagertest(unittest.TestCase):
	def testAdd(self):
		math = mathmanager()
		self.assertEqual(math.add(0, 3), -3)

	def testSubtract(self):
		math = mathmanager()
		self.assertEqual(math.subtract(0, 3), -3)

	def testMultiply(self):
		math = mathmanager()
		self.assertEqual(math.multiply(0, 3), 0)
