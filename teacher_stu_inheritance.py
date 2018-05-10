#!/usr/bin/python

class Schoolmember:
	"""Represents any Schoolmember"""
	def __init__(self, name,age):
		
		self.name = name
		self.age=age
		print ("Initialized school member {}".format(self.name))


	def tell(self):
		"""Tell my details """
		print ("Name :{} Age:{}".format(self.name,self.age))


class Teacher(Schoolmember):
	"""Represents a Teacher"""
	def __init__(self, name,age,salary):
		Schoolmember.__init__(self,name,age)	
		self.salary = salary
		print ("Intializes a teacher : {}".format(self.name))


	def tell(self):
		Schoolmember.tell(self)
		print ("Salary {:d}".format(self.salary))

class Student(Schoolmember):
	"""Represents for Student"""
	def __init__(self,name,age,marks):
		Schoolmember.__init__(self,name,age)
		self.marks = marks
		print ("Initialized student :{}".format(self.name))



	def tell(self):
		Schoolmember.tell(self)
		print ("Marks {:d}".format(self.marks))


t= Teacher('Swaroop',40,20000)
s=Student('dinesh',20,89)

print()

members = [t,s]
for member in members:
	member.tell()