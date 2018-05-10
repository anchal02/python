#!/usr/bin/python

class Robot:
	"""Represents a Robot, with a name"""

	population =0

	def __init__(self, name):
		"""Initializes the data."""
		self.name = name
		print "(Initializing{})".format(self.name)

		Robot.population+=1

	def Die(self):
		"""I am dying """
		print ("{} is being destroyed".format(self.name))

		Robot.population-=1

		if Robot.population==0:
			print ("{} was the last one ".format(self.name))

		else:
			print ("there are still {:d} robots working ".format(Robot.population))


	def say_hi(self):
		"""Greeting by the Robot,

		yeah,they can do it."""

		print ("Greetings,my master called me {}".format(self.name))


	@classmethod

	def how_many(cls):
		"""print the current population """
		print ("wh have {:d} robots".format(cls.population))


droid1 = Robot("R2-R1")
droid1.say_hi()
droid1.how_many()

droid2= Robot("C-PS1")
droid2.say_hi()
Robot.how_many()

print("\n Robots can work here\n")

print ("Robots have finished their work,lets finish them")

droid1.Die()
droid2.Die()

Robot.how_many()
