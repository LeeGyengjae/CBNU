# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:44:08 2024

@author: Lenovo
"""

#교수님 추천 넘파이 책
#딥러닝 머신러닝을 위한 파이썬 넘파이
import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x)
type(x) #자료구조(Data Structure) 행렬(Array)

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x + y)
print(x - y)
print(x * y)
print(x / y)

A = np.array([[1, 2], [3, 4]])
print(A)
A.shape
A.dtype

B = np.array([[3, 0], [0, 6]])
A + B
A * B