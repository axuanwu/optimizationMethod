#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np


def f_gx(X):
    x1 = X[0, 0]
    x2 = X[1, 0]
    r1 = 10 * (x2 * x2 - x1 * x1)
    r2 = 1 - x1
    gx1 = 2 * r1 * (-10 * 2 * x1) + 2 * r2 * (-1)
    gx2 = 2 * r1 * 10 * 2 * x2
    return np.matrix([gx1, gx2]).T


def my_function(X):
    # fx = 3*x1^2+3*x2^2 - x1^2*x2
    x1 = X[0, 0]
    x2 = X[1, 0]
    r1 = 10 * (x2 * x2 - x1 * x1)
    r2 = 1 - x1
    return r1 * r1 + r2 * r2


def f_Gx(X):
    x1 = X[0, 0]
    x2 = X[1, 0]
    G00 = 1200 * x1 * x1 - 400 * x2 * x2 + 2
    G01 = -800 * x1 * x2
    G10 = -800 * x1 * x2
    G11 = 1200 * x2 * x2 - 400 * x1 * x1
    return np.matrix([[G00, G01], [G10, G11]])
