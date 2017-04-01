# coding:utf-8
# to avoid over feeding
import numpy as np
import theano
import theano.tensor as T
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt

# 神经元对象


class Layer:
    def __init__(self, inputs, in_size, out_size, activation_function=None):
        # 创建一个数组矩阵，存放神经元的权值，矩阵为:[in_size, out_size]
        self.W = theano.shared(np.random.normal(0, 1, (in_size, out_size)))
        self.b = theano.shared(np.zeros((out_size, )) + 0.1)
        self.Wx_plus_b = T.dot(inputs, self.W) + self.b
        self.activation_function = activation_function
        if self.activation_function is None:
            self.outputs = self.Wx_plus_b
        else:
            self.outputs = self.activation_function(self.Wx_plus_b)

def minmax_normalization(data):
    xs_max = np.max(data, axis=0)
    xs_min = np.min(data, axis=0)
    xs = (1 - 0) * (data - xs_min) / (xs_max - xs_min) + 0
    return xs

np.random.seed(100)
x_data = load_boston().data
# minmax normalization, rescale the inputs
x_data = minmax_normalization(x_data)
y_data = load_boston().target[:, np.newaxis]

