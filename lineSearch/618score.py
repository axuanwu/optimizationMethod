#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import math


class lineSearch:
    def __init__(self):
        # 需要进行线搜的目标函数
        self.A = np.eye(2)  # 定义一个 系数
        self.direction = np.matrix([3, 4]).T / math.sqrt(5)  # 线搜方向
        self.XS = np.matrix([3, 4]).T  # 起始位置
        self.sign = 1  # 方向
        self.XE = self.XS
        self.distance = 1
        self.GoldenNum = (math.sqrt(5) - 1) / 2
        self.ratio = (math.sqrt(5) - 1) * 0.5
        self.XG0 = 0  # 用于存储某个黄金分割点
        self.YG0 = 0  # 某个黄金分割点的函数值
        self.YXS = 0  # 区间开始的函数值
        self.YXE = 0  # 区间结束的函数值
        self.accuracy = 0.0001

    def my_function(self, X):
        # X 是一个N 维 变量组
        # A 是系数
        # y = X.T * A *  X ; A单位矩阵时等价于 (x1+x2)^2
        return sum(sum(np.dot(X.T, self.A) * X))

    # 找到线搜的初始区间
    def find_search_region(self):
        step = 1  # 初始步长
        # sign = 1
        YS = self.my_function(self.XS)
        XE = self.XS + step * self.direction * self.sign  # 假设的结束位置
        YE = self.my_function(XE)
        if YE < YS:
            while True:
                step /= 0.5  # 加大步长
                XEN = XE + step * self.direction * self.sign
                YEN = self.my_function(XEN)
                XE = XEN
                if YEN > YE:
                    break
            self.XE = XE
            self.distance =float((self.XE - self.XS).T * self.direction)  # 有符号的距离可以为负数
        # return XE
        else:
            self.sign *= -1  # 反向搜索
            self.find_search_region()

    def final_solution(self):
        # 初始配置
        self.XG0 = self.XS + self.GoldenNum * self.distance * self.direction
        self.YG0 = self.my_function(self.XG0)
        self.YXS = self.my_function(self.XS)
        self.YXE = self.my_function(self.XE)
        while self.next_solution():
            print self.XG0, self.distance
        return self.XG0

    def next_solution(self):
        # 方法中一共包含四个点
        # XS 区间起点  XE 区间结束点 XG0 其中某一个黄金分割点 以上三个点均有上一步结果中继承下来
        # XG1 需要尝试的另外一个黄金分割点
        self.GoldenNum = 1 - self.GoldenNum
        XG1 = self.XS + self.GoldenNum * self.distance * self.direction  # 找到另一个点
        YG1 = self.my_function(XG1)
        if YG1 > self.YG0:
            if self.GoldenNum < 0.5:  # G1点切换为开始点 G0 保持 分割比 结束点保持 距离缩小
                self.XS = XG1
                self.YXS = YG1
                self.distance *= self.ratio
            else:  # G1 切换为结束点 G0保持 分割比 保持 开始点保持 距离缩小
                self.XE = XG1
                self.YXE = YG1
                self.distance *= self.ratio
        else:
            if self.GoldenNum < 0.5:  # G0点切换为结束点 G1切换为self.G0 1-分割比 开始点保持 距离缩小
                self.XE = self.XG0
                self.YXE = self.YG0
                self.XG0 = XG1
                self.YG0 = YG1
                self.GoldenNum = 1 - self.GoldenNum
                self.distance *= self.ratio
            else:  # G1 切换为开始点 G1切换为G0  1-分割比 保持 结束点保持 距离缩小
                self.XS = self.XG0
                self.YXS = self.YG0
                self.XG0 = XG1
                self.YG0 = YG1
                self.GoldenNum = 1 - self.GoldenNum
                self.distance *= self.ratio
        if abs(self.distance) > self.accuracy:
            return True
        else:
            return False

    def test_solution(self):
        x0 = self.XG0 + self.accuracy * self.direction
        x1 = self.XG0 - self.accuracy * self.direction
        if self.my_function(x0) > self.my_function(self.XG0) and self.my_function(x1) > self.my_function(self.XG0):
            return True  # 通过校验
        else:
            return False


if __name__ == "__main__":
    aa = lineSearch()
    aa.find_search_region()  # 找搜索区间
    print aa.final_solution()  # 线搜最优解
    print aa.test_solution()  # 测试结果是否满足 "高低高" 属性
