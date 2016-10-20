#!/usr/bin/python
# -*- coding: utf-8 -*-
import lineSearch
import numpy as np
import math


class Newton2:
    def __init__(self):
        # 需要进行线搜的目标函数
        self.A = 0
        self.X = np.matrix([3, 4]).T  # 初始的迭代点
        self.H = np.eye(2)  # 初始 H 矩阵  满足正定即可
        self.gx = np.matrix([0, 0]).T
        self.dk = np.matrix([0, 0]).T
        self.accuracy = 0.001
        self.myLineSearch = lineSearch.lineSearch()


    # # 函数方程
    def function(self, X):
        # fx = 3*x1^2+3*x2^2 - x1^2*x2
        x1 = X[0, 0]
        x2 = X[1, 0]
        r1 = 10 * (x2 * x2 - x1 * x1)
        r2 = 1 - x1
        return r1 * r1 + r2 * r2


    def f_gx(self):
        x1 = self.X[0, 0]
        x2 = self.X[1, 0]
        r1 = 10 * (x2 * x2 - x1 * x1)
        r2 = 1 - x1
        gx1 = 2 * r1 * (-10 * 2 * x1) + 2 * r2 * (-1)
        gx2 = 2 * r1 * 10 * 2 * x2
        self.gx = np.matrix([gx1, gx2]).T

    def f_Gx(self):
        x1 = self.X[0, 0]
        x2 = self.X[1, 0]
        G00 = 1200*x1*x1 - 400 * x2*x2 +2
        G01 = -800*x1*x2
        G10 = -800*x1*x2
        G11 = 1200*x2*x2 -400*x1*x1
        return np.matrix([[G00,G01],[G10,G11]])

    def final_solution(self):
        # 初始配置
        # self.H = self.f_Gx()
        print self.X.T  # 打印搜索轨迹
        while self.next_solution():
            print self.X.T


    def next_solution(self):
        # 迭代一次
        self.f_gx()
        self.dk = np.dot(self.H, self.gx)
        self.dk = self.dk / np.linalg.norm(self.dk)  # 归一化
        # 线搜索
        XK0 = self.X.copy()
        self.myLineSearch.direction = self.dk.copy()  # 初始化方向
        self.myLineSearch.XS = self.X.copy()  # 初始化起点
        self.myLineSearch.find_search_region()
        Xk1 = self.myLineSearch.final_solution()  #
        print self.myLineSearch.test_solution()
        gk0 = self.gx.copy()
        self.X = Xk1
        self.f_gx()
        gk1 = self.gx
        Sk = Xk1 - XK0
        Yk = gk1 - gk0
        Hk0 = self.H
        Hk1 = Hk0 + float(1 + float(np.dot(np.dot(Yk.T, Hk0), Yk)) / float(np.dot(Yk.T, Sk))) * np.dot(Sk,Sk.T) \
            / float( np.dot(Yk.T, Sk)) - (np.dot(np.dot(Sk, Yk.T), Hk0) - np.dot(np.dot(Hk0, Yk), Sk.T)) / float(np.dot(Yk.T, Sk))
        self.H = Hk1
        a = np.linalg.norm(gk1.T)
        if a > self.accuracy:
            return True
        else:
            return False


if __name__ == "__main__":
    aa = Newton2()
    aa.final_solution()  # 找最优解