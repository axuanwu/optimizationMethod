#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np

G = np.diag([1, 5, 10, 20])
B = np.matrix([0, 0, 0, 0]).T


def f_gx(X):
    return G * X + B


def my_function(X):
    return float(0.5 * X.T * G * X + B.T * X)
