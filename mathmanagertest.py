import unittest
from mathmanager import mathmanager

class mathmanagertest(unittest.TestCase):
	def testAdd(self):
		math = mathmanager()
		self.assertEqual(math.add(0, 3), 3)

	def testSubtract(self):
		math = mathmanager()
		self.assertEqual(math.subtract(0, 3), -3)

	def testMultiply(self):
		math = mathmanager()
		self.assertEqual(math.multiply(0, 3), 0)

	def test_income_tax_calculator(self):
		math = mathmanager()
		self.assertEqual(math.income_tax_calculator(12570), 0)
		self.assertEqual(math.income_tax_calculator(12571), 2514.2)
		self.assertEqual(math.income_tax_calculator(50270), 10054)
		self.assertEqual(math.income_tax_calculator(50271), 20108.4)
		self.assertEqual(math.income_tax_calculator(50270), 10054)
		self.assertEqual(math.income_tax_calculator(125140), 50056)
		self.assertEqual(math.income_tax_calculator(125141), 56313.45)

	def test_degree_classification(self):
		math = mathmanager()
		self.assertEqual(math.degree_classification(39, 39, 39, 39), "Fail")
		self.assertEqual(math.degree_classification(40, 40, 40, 40), "3rd")
		self.assertEqual(math.degree_classification(50, 50, 50, 50), "2:2")
		self.assertEqual(math.degree_classification(60, 60, 60, 60), "2:1")
		self.assertEqual(math.degree_classification(70, 70, 70, 70), "1st")



