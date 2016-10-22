#!/usr/bin/python
# -*- coding: utf-8 -*-
# import numpy as np
from myfunction import *


class BBsearch:
    def __init__(self):
        self.X = np.matrix([1, 1, 1, 1]).T
        pass

    def getAlpha(self):
        pass


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
