import unittest
from mathmanager import mathmanager

class mathmanagertest(unittest.TestCase):
	def testAdd(self):
		math = mathmanager()
      self.assertEqual(math.add(0, 3), 3)
