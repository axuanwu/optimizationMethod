#!/usr/bin/python
# -*- coding: utf-8 -*-
from lineSearch import lineSearch  # 精确线搜
# from wolfSearchStrong import lineSearch  # wolf 非精确线搜
# from wolfSearch import lineSearch  # wolf 非精确线搜

# import numpy as np
from function2dim2 import *


# import wolfSearch

class Newton2:
    def __init__(self):
        # 需要进行线搜的目标函数
        self.A = 0
        self.X = np.matrix([-1.2, 1]).T  # 初始的迭代点
        self.H = np.eye(2)  # 初始 H 矩阵  满足正定即可
        self.gx = np.matrix([0, 0]).T
        self.dk = np.matrix([0, 0]).T
        self.accuracy = 0.001
        self.myLineSearch = lineSearch()
        # self.myWolfSearch = wolfSearch.lineSearch()

    def final_solution(self):
        # 初始配置
        # self.H = self.f_Gx()
        print self.X.T  # 打印搜索轨迹
        i=0
        while self.next_solution():
            print i, self.X.T
            i+=1
            pass

    def next_solution(self):
        # 迭代一次
        self.gx = f_gx(self.X)
        self.dk = -np.dot(self.H, self.gx)
        self.dk /= np.linalg.norm(self.dk)  # 归一化
        # 线搜索
        XK0 = self.X.copy()
        self.myLineSearch.direction = self.dk.copy()  # 初始化方向
        self.myLineSearch.XS = self.X.copy()  # 初始化起点
        Xk1 = self.myLineSearch.final_solution()  #
        # print self.myLineSearch.test_solution()
        gk0 = self.gx.copy()
        self.X = Xk1
        self.gx = f_gx(self.X)
        gk1 = self.gx
        Sk = Xk1 - XK0
        Yk = gk1 - gk0
        Hk0 = self.H
        Hk1 = Hk0 + float(1 + float(np.dot(np.dot(Yk.T, Hk0), Yk)) / float(np.dot(Yk.T, Sk))) * np.dot(Sk, Sk.T) \
            / float(np.dot(Yk.T, Sk)) - (np.dot(np.dot(Sk, Yk.T), Hk0) - np.dot(np.dot(Hk0, Yk), Sk.T)) / float(np.dot(Yk.T, Sk))
        self.H = Hk1
        a = np.linalg.norm(gk1)
        if a > self.accuracy:
            return True
        else:
            return False


if __name__ == "__main__":
    aa = Newton2()
    aa.final_solution()  # 找最优解
