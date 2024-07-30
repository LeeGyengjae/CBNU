# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:25:29 2024

@author: Lenovo
"""

import sys, os
sys.path.append(os.pardir)
import tensorflow as tf
#from tensorflow.python.keras.datasets.mnist import load_mnist

#(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
(x_train, t_train), (x_test, t_test) = tf.keras.datasets.mnist.load_mnist(flatten=True, normalize=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)