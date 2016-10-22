#!/usr/bin/python
# -*- coding: utf-8 -*-
# import numpy as np
from myfunction import *


class BBsearch:
    def __init__(self):
        self.X = np.matrix([1.0, 1, 1, 1]).T
        self.gk = np.matrix([1.0, 1, 1, 1]).T
        self.accuracy = 10**-8
        self.alpha = 0
        self.i = 0
        pass

    @property
    def getAlpha(self):
        return float(self.gk.T * self.gk)/float(self.gk.T * G * self.gk)

    # 设置初始点
    def set_first(self, X):
        self.X = np.matrix(X).T
        self.gk = f_gx(self.X)

    def final_solution(self):
        # 初始配置
        self.set_first([1.0, 1, 1, 1])
        # print i,self.getAlpha, my_function(self.X)  # 打印搜索轨迹
        while self.next_solution():
            pass
            # print i,self.alpha, my_function(self.X)

    def next_solution(self):
        # 迭代一次
        # 先计算 alpha 再更新 gk
        self.alpha = self.getAlpha
        self.gk = f_gx(self.X)
        print self.i, self.alpha, my_function(self.X)  # 打印收敛轨迹
        self.i += 1
        self.X -= self.alpha * self.gk
        a = np.linalg.norm(self.gk)
        if a > self.accuracy:
            return True
        else:
            return False

if __name__ == "__main__":
    aa = BBsearch()
    aa.final_solution()  # 找最优解
