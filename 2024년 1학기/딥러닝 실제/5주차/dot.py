# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:35:31 2024

@author: Lenovo
"""

import numpy as np

A = np.array([[1, 2], [3, 4]])
A.shape

B = np.array([[5, 6], [7, 8]])
B.shape

X = np.dot(A, B)
print(X)