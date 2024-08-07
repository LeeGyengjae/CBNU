# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:24:39 2024

@author: Lenovo
"""

import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

#수치미분
def function_1(x):
    return 0.01*x**2 + 0.1*x

#편미분
def function_2(x):
    return x[0]**2 + x[1]**2

def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

def function_tmp2(x1):
    return 3.0**2.0 + x1*x1

x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()

r = numerical_diff(function_1, 5)
print(r)

r = numerical_diff(function_1, 10)
print(r)


r = numerical_diff(function_tmp1, 3.0)
print(r)

r = numerical_diff(function_tmp2, 4.0)
print(r)