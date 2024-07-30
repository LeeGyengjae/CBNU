# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:17:37 2024

@author: Lenovo
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, lable='sin')
plt.plot(x, y2, linestyle='--', label='cos')