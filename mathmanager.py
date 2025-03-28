class mathmanager:

	def add(self, a, b):
			return a+b

	def subtract(self, a, b):
			return a-b

	def multiply(self, a, b):
			return a*b

	def income_tax_calculator(self, income):
		if income <= 12570:
			tax_multiplier = 0
		elif income <= 50270:
			tax_multiplier = 0.2
		elif income <= 125140:
			tax_multiplier = 0.4
		else:
			tax_multiplier = 0.45
		return tax_multiplier * income
	
	def degree_classification(self, m1, m2, m3, m4):
		avg = (m1 + m2 + m3 + m4) / 4
		if avg < 40:
			return "Fail"
		elif avg < 50:
			return "3rd"
		elif avg < 60:
			return "2:2"
		elif avg < 70:
			return "2:1"
		else:
			return "1st"