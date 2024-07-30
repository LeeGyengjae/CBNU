# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:13:44 2024

@author: Lenovo
"""

import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array( x > 0, dtype=np.int32)

def sigmoid(x):
    return 1 / ( 1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)

y = step_function(x)
plt.plot(x, y)

y2 = sigmoid(x)
plt.plot(x, y2)

plt.ylim(-0.1, 1.1)
plt.show

