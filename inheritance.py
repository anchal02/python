#!/usr/bin/python

class Parent:
	parentAttr = 100

	def __init__(self):
		print "calling parent constructor"

	def parentMethod(self):
		print "calling parent method"

	def setAttr(self,attr):
		Parent.parentAttr=attr

	def getAttr(self):
		print "Parent Attr: ", Parent.parentAttr


class Child(Parent):
	def __init__(self):
		print "calling child constructor"

	def ChildMethod(self):
		print "calling child method"

c = Child()
c.ChildMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()