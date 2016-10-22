#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import math


class Newton:
	def __init__(self):
		# 参数
		self.A = 0
		self.X = np.matrix([0, 0]).T
		self.gx = np.matrix([0, 0]).T
		self.Gx = np.zeros((2, 2))
		self.accuracy = 0.00001

	# # 函数方程
	def function(self, X):
		# fx = 3*x1^2+3*x2^2 - x1^2*x2
		x1 = X[0, 0]
		x2 = X[1, 0]
		return 3 * x1 * x1 + 3 * x2 * x2 - x1 * x1 * x2

	#  梯度
	def g_fun(self):
		x1 = self.X[0, 0]
		x2 = self.X[1, 0]
		x10 = 6 * x1 - 2 * x1 * x2
		x20 = 6 * x2 - x1 * x1
		self.gx = np.matrix([x10, x20]).T

	# 2阶导数
	def G_fun(self):
		x1 = self.X[0, 0]
		x2 = self.X[1, 0]
		self.Gx = np.matrix([[6 - 2 * x2, -2 * x1], [-2 * x1, 6]])

	# 求解牛顿方程
	def dk_fun(self):
		# 牛顿方程求最优解 dk = -inv(G)*gk
		return -1 * np.dot(self.Gx.I, self.gx)

	# 设置初始点
	def set_first(self, X):
		self.X = np.matrix(X).T

	def final_solution(self):
		# 初始配置
		print self.X.T  # 打印搜索轨迹
		while self.next_solution():
			print self.X.T

	def next_solution(self):
		# 迭代一次
		self.G_fun()
		self.g_fun()
		self.X = self.X + self.dk_fun()
		a = np.linalg.norm(self.gx.T)
		if a > self.accuracy:
			return True
		else:
			return False

if __name__ == "__main__":
	aa = Newton()
	aa.set_first([1.5, 1.5])
	aa.final_solution()  # 找最优解


