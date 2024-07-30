# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 19:00:57 2024

@author: Lenovo
"""
import numpy as np

def sum_squares_error(y, t):
    return 0.5 * np.sum((y-t)**2)

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
r = sum_squares_error(np.array(y), np.array(t))

print(r)

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
r = sum_squares_error(np.array(y), np.array(t))

print(r)
