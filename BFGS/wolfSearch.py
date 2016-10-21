#!/usr/bin/python
# -*- coding: utf-8 -*-

from function2dim import *
import math


class lineSearch:
    def __init__(self):
        self.direction = np.matrix([1, 2]).T / math.sqrt(5)  # 线搜方向
        self.XS = np.matrix([3, 4]).T  # 起始位置
        self.leftBound = 0
        self.Max = 4
        self.rightBound = self.Max
        pass

    def final_solution(self):
        # self.direction /= np.linalg.norm(self.direction)  # 单位化
        c1 = 0.1
        c2 = 0.9
        iter0 = 0
        alpha = 0.1
        x0 = self.XS.copy()
        fx0 = my_function(x0)
        gx0 = f_gx(x0)
        dd0 = float(np.dot(gx0.T, self.direction))
        # xt = x0 + alpha * self.direction
        while iter0 < 100:
            xt = x0 + alpha * self.direction
            # print iter0, xt
            fxt = my_function(xt)
            gxt = f_gx(xt)
            ddt = float(np.dot(gxt.T, self.direction))
            iter0 += 1
            if fxt >= (fx0+c1 * alpha * dd0):
                self.rightBound = alpha
                alpha = (self.leftBound+self.rightBound) * 0.5
            elif ddt <= c2 * dd0:
                self.leftBound = alpha
                alpha = (self.leftBound + self.rightBound) * 0.5
            else:
                break
        print (x0 + alpha * self.direction).T
        return x0 + alpha * self.direction
