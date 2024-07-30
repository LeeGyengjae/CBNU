# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:06:24 2024

@author: Lenovo
"""

import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t*np.log(y + delta))

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
r = cross_entropy_error(np.array(y), np.array(t))

print(r)

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
r = cross_entropy_error(np.array(y), np.array(t))

print(r)