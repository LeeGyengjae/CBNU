# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:08:33 2024

@author: Lenovo
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
#y = np.sin(x)
y = np.cos(x)

plt.plot(x, y)
plt.show()