# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:37:17 2024

@author: Lenovo
"""
import numpy as np

a = np.array([0.3, 2.9, 4.0])

exp_a = np.exp(a)
print(exp_a)

sum_exp_a = np.sum(exp_a)
print(sum_exp_a)

y = exp_a / sum_exp_a
print(y)