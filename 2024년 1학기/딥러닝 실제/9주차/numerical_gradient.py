# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:05:24 2024

@author: Lenovo
"""

import numpy as np
import matplotlib.pylab as plt

#수치미분
def function_1(x):
    return 0.01*x**2 + 0.1*x

#편미분
def function_2(x):
    return x[0]**2 + x[1]**2

def numerical_gradient(f,x):
    h = 1e-4
    grad = np.zeros_like(x)
    
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)
        
        x[idx] = tmp_val - h
        fxh2 = f(x)
        
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val
        
    return grad

r = numerical_gradient(function_2, np.array([3.0, 4.0]))
print(r)

r = numerical_gradient(function_2, np.array([0.0, 2.0]))
print(r)

r = numerical_gradient(function_2, np.array([3.0, 0.0]))
print(r)