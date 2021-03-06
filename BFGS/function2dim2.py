#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np


def f_gx(X):
    x1 = X[0, 0]
    x2 = X[1, 0]
    r1 = 10 * (x2  - x1 * x1)
    r2 = 1 - x1
    gx1 = 2 * r1 * (-10 * 2 * x1) + 2 * r2 * (-1)
    gx2 = 2 * r1 * 10
    return np.matrix([gx1, gx2]).T


def my_function(X):
    # fx = 3*x1^2+3*x2^2 - x1^2*x2
    x1 = X[0, 0]
    x2 = X[1, 0]
    r1 = 10 * (x2  - x1 * x1)
    r2 = 1 - x1
    return r1 * r1 + r2 * r2



