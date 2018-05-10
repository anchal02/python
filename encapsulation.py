#!/usr/bin/python

class Computer:
	"""docstring for Computer"""
	def __init__(self):
		
		self.__maxprice = 900

	def sell(self):
		print ("Selling Price :{}".format(self.__maxprice))

	def maxprixe(self,price):
		self.__maxprice = price


c=Computer ()
c.sell()

c.__maxprice=100
c.sell()

c.maxprixe(1000)
c.sell()