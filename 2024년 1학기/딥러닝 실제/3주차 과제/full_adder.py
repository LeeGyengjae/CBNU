# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:05:57 2024

@author: Lenovo
"""
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

def full_adder(x1, x2, carry):
    sum_bit = XOR(XOR(x1, x2), carry)
    carry_out = OR(AND(XOR(x1, x2), carry), AND(x1, x2))
    return sum_bit, carry_out


result = full_adder(1, 1, 1)
print("Sum bit:", result[0])
print("Carry bit:", result[1])
