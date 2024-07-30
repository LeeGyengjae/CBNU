# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:26:58 2024

@author: Lenovo
"""

import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)

y = relu(x)
plt.plot(x, y)

plt.ylim(-1, 6)
plt.xlim(-6, 6)
plt.show