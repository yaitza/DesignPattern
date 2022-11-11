#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/11 09:43
# @Author  : 杨智杰
# @Email   : yangzhijie@datagrand.com

from burger import *

class FoodFactory():
	type = ""

	def createFood(self, foodClass):
		print(self.type, " factory produce a instance")
		foodIns = foodClass()
		return foodIns

class BurgerFactory(FoodFactory):
	def __init__(self):
		self.type = "BURGER"

class SnackFactory(FoodFactory):
	def __init__(self):
		self.type = "SNACK"

class BeverageFactory(FoodFactory):
	def __init__(self):
		self.type = "BEVERAGE"

if __name__ == "__main__":
	burger_factory = BurgerFactory()
	cheese_burger = burger_factory.createFood(CheeseBurger)
	print(cheese_burger.getName(), cheese_burger.getPrice())