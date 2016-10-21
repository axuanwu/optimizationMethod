#!/usr/bin/python
# -*- coding: utf-8 -*-

from function2dim2 import *
import math


class lineSearch:
    def __init__(self):
        self.direction = np.matrix([1, 2]).T / math.sqrt(5)  # 线搜方向
        self.XS = np.matrix([3, 4]).T  # 起始位置
        self.leftBound = 0
        self.Max = 0.4
        self.rightBound = self.Max
        pass

    def final_solution(self):
        # self.direction /= np.linalg.norm(self.direction)  # 单位化
        rou = 0.0001
        sigma = 0.9
        iter0 = 0
        alpha = 0.2
        x0 = self.XS.copy()
        fx0 = my_function(x0)
        gx0 = f_gx(x0)
        dd0 = float(np.dot(gx0.T, self.direction))
        xt = x0 + alpha * self.direction
        while iter0 < 100:
            xt = x0 + alpha * self.direction
            # print iter0, xt
            fxt = my_function(xt)
            gxt = f_gx(xt)
            ddt = float(np.dot(gxt.T, self.direction))
            iter0 += 1
            if fxt > (fx0+rou * alpha * dd0):
                self.rightBound = alpha
                alpha = (self.leftBound+self.rightBound) * 0.5
            elif ddt < (sigma * dd0):
                self.leftBound = alpha
                alpha = (self.leftBound + self.rightBound) * 0.5
            else:
                break
        # print (x0 + alpha * self.direction).T
        # print self.testSolution(xt,x0,rou,sigma,alpha)
        return xt

    def testSolution(self,xt,x0,rou,sigma,alpha):
        fxt = my_function(xt)
        fx0 = my_function(x0)
        gx0 = f_gx(x0)
        gxt = f_gx(xt)
        dd0 = float(np.dot(gx0.T, self.direction))
        ddt = float(np.dot(gxt.T, self.direction))
        if fxt <= (fx0+ rou * alpha * dd0):
            if ddt>=(sigma*dd0):
                return True
        return False
