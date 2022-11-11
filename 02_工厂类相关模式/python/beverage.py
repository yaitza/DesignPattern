#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/11 09:41
# @Author  : 杨智杰
# @Email   : yangzhijie@datagrand.com

class Beverage():
	name = ""
	price = 0.0

	def getPrice(self):
		return self.price

	def setPrice(self, value):
		self.price = value

	def getName(self):
		return self.name


class Coke(Beverage):
	def __init__(self):
		self.name = "chips"
		self.price = 6.0


class Milk(Beverage):
	def __init__(self):
		self.name = "chicken wings"
		self.price = 12.0