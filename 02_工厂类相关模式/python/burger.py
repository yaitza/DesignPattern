#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/11 09:37
# @Author  : 杨智杰
# @Email   : yangzhijie@datagrand.com

class Burger():
	name = ""
	price = 0.0

	def getPrice(self):
		return self.price

	def setPrice(self, value):
		self.price = value

	def getName(self):
		return self.name

class CheeseBurger(Burger):
	def __init__(self):
		self.name = 'cheese burger'
		self.price = 10.0

class SpicyChickenBurger(Burger):
	def __init__(self):
		self.name = "spicy chicken burger"
		self.price = 15.0