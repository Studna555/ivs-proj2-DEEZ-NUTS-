##
#	@File		mathpack.py
#	@Author		Jakub Zapletal \n
#				Faculty of Information Technology \n
#				Brno University of Technology \n
#				xzaple36@fit.vutbr.cz
#	@Brief		Mathematical library for calculator's operations
#	@Version	1.0 Final
#	@Date		13. 04. 2016 (created)\n
#				18. 04. 2016 (edited)
#
#	@Mainpage	Welcome to the project's documentation.	
#

#	@Defgroup	cls Classes
#	@Brief		All classes used in project

#	@Defgroup	ops	Operations
#	@Brief		Mathematical operations used in the calculator


##
#	Class of mathematical library containing all mathematical operations
#	@Brief		Class of mathematical library
#	#Ingroup	cls
class Maths:

	ans = 0 


	##
	#	Function adds up all entered numbers and returns the result
	#	@Brief		Sum of all entered numbers
	#	@Ingroup	ops
	#
	#	@Param[in,out] self	Method instance
	#	@Param[in] numbers Array of entered numbers
	#
	#	@Return Result of the add up
	def add(self, numbers):
		result = 0
		for number in numbers:
			result += number
		self.ans = result


	##
	#	Function substracts all numbers and returns the result
	#	@Brief		Substract of all entered numbers
	#	@Ingroup	ops
	#
	#	@Param[in,out] self	Method instance
	#	@Param[in] numbers Array of entered numbers
	#
	#	@Return Result of the substraction
	def substract(self, numbers):
		result = numbers[0]
		iternum = iter(numbers)
		next(iternum)
		for number in iternum: 
			result -= number
		self.ans = result


	##
	#	Function multiplies entered numbers and returns the result
	#	@Brief		Multiplication of all entered numbers
	#	@Ingroup	ops
	#
	#	@Param[in,out] self	Method instance
	#	@Param[in] numbers Array of entered numbers
	#
	#	@Return Result of the multiplication
	def mult(self, numbers):
		result = numbers[0]
		iternum = iter(numbers)
		next(iternum)
		for number in iternum: 
			result *= number
		self.ans = result


	##
	#	Function divides Dividend with Factor and returns the result
	#	@Brief		Division of two numbers
	#	@Ingroup	ops
	#
	#	@Param[in,out] self	Method instance
	#	@Param[in] dividend Dividend
	#	@Param[in] factor 	Factor
	#
	#	@Return Result of the division
	def div(self, dividend, factor):
		if dividend == factor:
			self.ans = 1
			return
		if factor == 0:
			self.ans = None
			return
		self.ans = dividend/factor


	##
	#	Function counts the residue after devision Dividend with Factor and returns the result
	#	@Brief		Modulo of entered numbers
	#	@Ingroup	ops
	#
	#	@Param[in,out] self	Method instance
	#	@Param[in] dividend Dividend
	#	@Param[in] factor 	Factor
	#
	#	@Return Result of the modulo operation
	def modulo(self, dividend, factor):
		if factor == 0:
			self.ans = None
			return
		self.ans = dividend % factor


	##
	#	Function intensified entered number on an exponent and returns the result
	#	@Brief		Pow number on exponent
	#	@Ingroup	ops
	#
	#	@Param[in,out] self	Method instance
	#	@Param[in] number 	Number to pow
	#	@Param[in] exponent	Exponent
	#
	#	@Return Result of the power operation
	def pow(self, number, exponent):
		result = number
		if exponent == 0:
			self.ans = 1
			return
		for i in range(1, abs(exponent)):
			result *= number
		if exponent < 0:
			self.ans = 1.0/result
			return
		self.ans = result


	##
	#	Function counts the factorial of entered number and returns the result
	#	@Brief		Factorial of an entered number
	#	@Ingroup	ops
	#
	#	@Param[in,out] self	Method instance
	#	@Param[in] number Entered number
	#
	#	@Return Result of the factorial
	def factorial(self, number):
		result = 1
		if isinstance(number, float):
			self.ans = None
			return
		if number == 0:
			self.ans = result
			return
		if number < 0:
			self.ans = None
			return
		if number > 10:
			self.ans = None
			return
		for i in range(1, number+1):
			result *= i
		self.ans = result