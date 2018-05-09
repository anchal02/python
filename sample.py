#!/usr/bin/python

class Emp:
	'common base class for all employees'
	empCount = 0

	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
		Emp.empCount += 1

	def Displaycount(self):
		print " number of %d employees" %Emp.empCount	

	def DisplayEmployee(self):
		print " name ", self.name , "salary " ,self.salary
	
emp1 = Emp("Zara",2000)
emp2 = Emp("lulu",4000)

emp1.DisplayEmployee()
emp2.DisplayEmployee()
print "Total Employee %d" %Emp.empCount

print "Emp.__doc__:", Emp.__doc__
print "Emp.__name__:", Emp.__name__
print "Emp.__module__:", Emp.__module__
print "Emp.__bases__:", Emp.__bases__
print "Emp.__dict__:", Emp.__dict__
