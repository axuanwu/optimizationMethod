#!/usr/bin/python
# -*- coding: utf-8 -*-
# 该方法是以618精确线搜为基础 结合wolf强准则
# 既然非精线搜只是找到一个满足准则的点来保证收敛性 ，怎么找这个点似乎并不是一个重点。
# 精确线搜虽然不依据准则的判断结果（反馈）来调整步长，但是总能找到这样的一个点满足准则
# 因此这里直接采用精确线搜的逻辑过程加上非精线搜的终止条件


from function2dim2 import *
import math


class lineSearch:
    def __init__(self):
        # 需要进行线搜的目标函数
        self.A = np.eye(2)  # 定义一个 系数
        self.direction = np.matrix([1, 2]).T / math.sqrt(5)  # 线搜方向
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

    # 找到线搜的初始区间
    def find_search_region(self):
        step = 0.001  # 初始步长
        # sign = 1
        YS = my_function(self.XS)
        XE = self.XS + step * self.direction * self.sign  # 假设的结束位置
        YE = my_function(XE)
        if YE < YS:
            while True:
                step /= 0.5  # 加大步长
                XEN = XE + step * self.direction * self.sign
                YEN = my_function(XEN)
                XE = XEN
                if YEN > YE:
                    break
            self.XE = XE
            self.distance = float((self.XE - self.XS).T * self.direction)  # 有符号的距离可以为负数
        # return XE
        else:
            self.sign *= -1  # 反向搜索
            step = 0.0001  # 初始步长
            # sign = 1
            YS = my_function(self.XS)
            XE = self.XS + step * self.direction * self.sign  # 假设的结束位置
            YE = my_function(XE)
            if YE < YS:
                while True:
                    step /= 0.5  # 加大步长
                    XEN = XE + step * self.direction * self.sign
                    YEN = my_function(XEN)
                    XE = XEN
                    if YEN > YE:
                        break
                self.XE = XE
                self.distance = float((self.XE - self.XS).T * self.direction)  # 有符号的距离可以为负数

    def final_solution(self):
        # 找到线搜区间
        self.find_search_region()
        X0 = self.XS.copy()
        fx0 = my_function(X0)
        gx0 = f_gx(X0)
        dd0 = float(np.dot(gx0.T, self.direction))
        rou = 0.0001
        sigma = 0.9
        iter0 = 0
        # 初始配置
        self.XG0 = self.XS + self.GoldenNum * self.distance * self.direction
        self.YG0 = my_function(self.XG0)
        self.YXS = my_function(self.XS)
        self.YXE = my_function(self.XE)
        while self.next_solution():
            iter0 += 1
            # 检查 wolf 准则
            Xt = self.XG0.copy()
            fxt = my_function(Xt)
            gxt = f_gx(Xt)
            ddt = float(np.dot(gxt.T, self.direction))
            alpha = float(np.dot((Xt - X0).T, self.direction))  # xt = x0 + alpha * self.direction ; direction为单位列向量
            if fxt <= (fx0 + rou * alpha * dd0):
                if abs(ddt) <= -sigma * dd0:
                    break
            if iter0 > 1000:
                break
        return Xt

    def next_solution(self):
        # 方法中一共包含四个点
        # XS 区间起点  XE 区间结束点 XG0 其中某一个黄金分割点 以上三个点均有上一步结果中继承下来
        # XG1 需要尝试的另外一个黄金分割点
        self.GoldenNum = 1 - self.GoldenNum
        XG1 = self.XS + self.GoldenNum * self.distance * self.direction  # 找到另一个点
        YG1 = my_function(XG1)
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
